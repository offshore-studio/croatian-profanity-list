#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Croatian / South Slavic profanity moderation dataset."""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "data"

DIACRITICS = str.maketrans({"č": "c", "ć": "c", "đ": "d", "š": "s", "ž": "z"})

FALSE_POSITIVE = {
    "u", "i", "a", "o", "se", "je", "te", "me", "mi", "ti", "on", "ona", "od", "do", "na", "po",
    "za", "iz", "kod", "kroz", "bez", "pri", "prema", "pa", "da", "ne", "ni", "no", "nu", "ga",
    "ju", "ih", "im", "si", "su", "smo", "ste", "bio", "bila", "bilo", "bili", "bile", "bit", "biti",
    "rat", "ser", "sera", "seru", "kur", "kurir", "pick", "bum", "debata", "idiom", "retorika",
    "glava", "glavica", "glavni", "stok", "govedina", "svinjetina", "ribica", "kakao", "duplex",
    "serija", "servis", "servirati", "mongol", "mongolija", "download", "pederastija",
}


def strip_diacritics(text: str) -> str:
    return text.translate(DIACRITICS)


def normalize(text: str) -> str:
    text = text.lower().translate(DIACRITICS)
    text = re.sub(r"[^a-z0-9]+", "", text)
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    return text.strip()


def has_diacritics(text: str) -> bool:
    return any(ch in text for ch in "čćđšžČĆĐŠŽ")


def stretch(word: str, repeats: tuple[int, ...] = (2, 3, 4)) -> set[str]:
    out = set()
    for i, ch in enumerate(word):
        if not ch.isalpha():
            continue
        for n in repeats:
            out.add(word[:i] + ch * n + word[i + 1 :])
    return out


def leet_variants(word: str) -> set[str]:
    subs = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"}
    out = set()
    lower = word.lower()
    for i, ch in enumerate(lower):
        if ch in subs:
            out.add(lower[:i] + subs[ch] + lower[i + 1 :])
    combos = [("a", "4"), ("e", "3"), ("i", "1"), ("o", "0"), ("s", "5")]
    for a, b in combos:
        if a in lower:
            out.add(lower.replace(a, b))
    return out


def punct_bypass(word: str) -> set[str]:
    chars = list(word)
    out = {
        ".".join(chars),
        "-".join(chars),
        "_".join(chars),
        " ".join(chars),
        "*".join(chars),
    }
    if len(word) > 2:
        out.add(word[0] + "*" + word[1:])
        out.add(word[:2] + "." + word[2:])
    return out


def misspell(word: str) -> set[str]:
    out = set()
    if len(word) > 3:
        out.add(word + word[-1])
        out.add(word + "m")
        out.add(word + "mm")
        out.add(word[:-1] + word[-1] * 2)
    if "ck" in word:
        out.add(word.replace("ck", "kk"))
    if "c" in word:
        out.add(word.replace("c", "k", 1))
    if "k" in word:
        out.add(word.replace("k", "c", 1))
    return out


def verb_ati(stem: str) -> set[str]:
    if stem.endswith("ati"):
        base = stem[:-3]
    elif stem.endswith("iti"):
        base = stem[:-3]
    else:
        base = stem.rstrip("i")
        if base.endswith("a"):
            base = base[:-1]
    forms = {
        stem,
        base + "em",
        base + "eš",
        base + "es",
        base + "e",
        base + "emo",
        base + "ete",
        base + "u",
        base + "ao",
        base + "ala",
        base + "alo",
        base + "ali",
        base + "ale",
        base + "aj",
        base + "ajmo",
        base + "ajte",
        base + "ajući",
        base + "an",
        base + "anje",
        base + "anja",
        base + "anju",
        base + "anjem",
        base + "i",
        base + "imo",
        base + "ite",
        base + "at",
        base + "at cu",
        base + "at ću",
    }
    if stem.startswith("zajeb") or base.startswith("zajeb"):
        forms.update({"zajeb", "zajebana", "zajebancija", "zajebancijo"})
    return forms


def noun_masc(word: str) -> set[str]:
    root = word
    if root.endswith("ac"):
        stem = root[:-2]
        return {
            root,
            stem + "ca",
            stem + "cu",
            stem + "cem",
            stem + "ci",
            stem + "aca",
            stem + "cima",
            stem + "ce",
        }
    if root.endswith("ar"):
        stem = root[:-2]
        return {root, stem + "ra", stem + "ru", stem + "rem", stem + "ri", stem + "ara", stem + "rima"}
    return {root, root + "a", root + "u", root + "om", root + "e", root + "i", root + "ima"}


def noun_fem(word: str) -> set[str]:
    if word.endswith("a"):
        stem = word[:-1]
        return {word, stem + "e", stem + "u", stem + "om", stem + "i", stem + "ama", stem + "o"}
    return {word, word + "e", word + "u", word + "om", word + "i"}


def expand_base(word: str, kind: str) -> set[str]:
    w = word.lower()
    forms = {w}
    if kind == "verb_ati":
        forms |= verb_ati(w)
    elif kind == "verb_iti":
        stem = w[:-3] if w.endswith("iti") else w
        forms |= {w, stem + "im", stem + "is", stem + "i", stem + "imo", stem + "ite", stem + "e"}
    elif kind == "noun_m":
        forms |= noun_masc(w)
    elif kind == "noun_f":
        forms |= noun_fem(w)
    elif kind in {"adj", "slur", "phrase", "expression"}:
        forms.add(w)
    nd = strip_diacritics(w)
    if nd != w:
        forms.add(nd)
    no_diac = {strip_diacritics(f) for f in list(forms)}
    forms |= no_diac
    return {f.strip() for f in forms if f and len(f) >= 2}


def build_regex_pattern(normalized_root: str) -> str:
    parts = []
    for ch in normalized_root:
        group = [re.escape(ch)]
        if ch in "aeios":
            alt = {"a": "4@", "e": "3", "i": "1!", "o": "0", "s": "5$"}.get(ch)
            if alt:
                group.append(alt)
        parts.append("[" + "".join(group) + "]")
    core = "".join(parts)
    last = re.escape(normalized_root[-1]) if normalized_root else ""
    return rf"(?<![a-z0-9]){core}(?:{last}){{0,3}}(?![a-z0-9])"


def make_entry(root: str, variant: str, severity: int, category: str, locales: list[str], obfuscated: bool) -> dict | None:
    norm = normalize(variant)
    if len(norm) < 2 or norm in FALSE_POSITIVE:
        return None
    return {
        "root": root,
        "variant": variant,
        "normalized": norm,
        "severity": severity,
        "category": category,
        "locale": sorted(set(locales)),
        "contains_diacritics": has_diacritics(variant),
        "obfuscated": obfuscated,
        "generated": True,
    }


def load_seeds() -> list[tuple[str, int, str, list[str], str]]:
    import sys

    src_dir = Path(__file__).resolve().parent
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))
    from hr_profanity_seeds import SEEDS  # noqa: WPS433

    return [(a, b, c, list(d), e) for a, b, c, d, e in SEEDS]


def compound_bypass(phrase: str) -> set[str]:
    words = phrase.split()
    if len(words) < 2:
        return set()
    return {
        ".".join(words),
        "-".join(words),
        "_".join(words),
        "*".join(words),
        "  ".join(words),
        " ".join(words),
    }


def generate_variants(base_form: str) -> list[tuple[str, bool]]:
    variants: list[tuple[str, bool]] = [(base_form, False)]
    if " " in base_form:
        for v in compound_bypass(base_form):
            variants.append((v, True))
        nd = strip_diacritics(base_form)
        if nd != base_form:
            variants.append((nd, False))
            for v in compound_bypass(nd):
                variants.append((v, True))
        return variants
    for v in stretch(base_form):
        variants.append((v, True))
    for v in leet_variants(base_form):
        variants.append((v, True))
    for v in punct_bypass(base_form):
        variants.append((v, True))
    for v in misspell(base_form):
        variants.append((v, True))
    nd = strip_diacritics(base_form)
    if nd != base_form:
        variants.append((nd, False))
    return variants


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    entries: dict[str, dict] = {}
    root_set: set[str] = set()
    regex_map: dict[str, dict] = {}

    for lemma, severity, category, locales, kind in load_seeds():
        root_set.add(lemma)
        for base in expand_base(lemma, kind):
            for variant, obfuscated in generate_variants(base):
                entry = make_entry(lemma, variant, severity, category, locales, obfuscated)
                if not entry:
                    continue
                key = entry["variant"].lower() + "|" + lemma + "|" + category
                if key not in entries:
                    entries[key] = entry
                elif entry["severity"] > entries[key]["severity"]:
                    entries[key] = entry
                elif entry["severity"] == entries[key]["severity"] and entries[key]["obfuscated"] and not entry["obfuscated"]:
                    entries[key] = entry
                norm_root = normalize(lemma)
                if norm_root and len(norm_root) >= 3 and norm_root not in FALSE_POSITIVE:
                    regex_map.setdefault(norm_root, {
                        "root": lemma,
                        "normalized": norm_root,
                        "pattern": build_regex_pattern(norm_root),
                        "severity": severity,
                        "category": category,
                        "locale": sorted(set(locales)),
                    })

    dataset = sorted(entries.values(), key=lambda x: (x["normalized"], x["root"], x["category"]))
    regex_list = sorted(regex_map.values(), key=lambda x: x["normalized"])

    meta = {
        "language": "hr",
        "locales": ["HR", "BA", "RS", "ME"],
        "total_entries": len(dataset),
        "unique_roots": len(root_set),
        "unique_normalized": len({e["normalized"] for e in dataset}),
        "generated_at": "2026-08-01",
        "version": "1.1.0",
    }

    (OUT_DIR / "profanity.json").write_text(
        json.dumps({"meta": meta, "entries": dataset}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    with (OUT_DIR / "profanity.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "root", "variant", "normalized", "severity", "category",
                "locale", "contains_diacritics", "obfuscated", "generated",
            ],
        )
        writer.writeheader()
        for row in dataset:
            writer.writerow({**row, "locale": "|".join(row["locale"])})

    (OUT_DIR / "profanity.txt").write_text(
        "\n".join(e["variant"] for e in dataset) + "\n",
        encoding="utf-8",
    )

    (OUT_DIR / "profanity.regex.json").write_text(
        json.dumps({
            "meta": {
                **meta,
                "flags": "iu",
                "notes": "Word-boundary patterns with leet, spacing, punctuation, and repeated-letter bypass tolerance.",
            },
            "patterns": regex_list,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Roots: {len(root_set)}")
    print(f"Entries: {len(dataset)}")
    print(f"Regex patterns: {len(regex_list)}")
    print(f"Output: {OUT_DIR}")


if __name__ == "__main__":
    main()
