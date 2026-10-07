#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export search-oriented Croatian profanity lists into lists/.

Reads data/profanity.json (+ regex) produced by generate_hr_profanity_dataset.py
and writes:

  lists/hr.txt
  lists/hr-phrases.txt
  lists/hr-normalized.txt
  lists/hr-regex.json
  lists/hr-severity.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = Path(__file__).resolve().parent
DATA_DIR = REPO_ROOT / "data"
LISTS_DIR = REPO_ROOT / "lists"
SRC_JSON = DATA_DIR / "profanity.json"
SRC_REGEX = DATA_DIR / "profanity.regex.json"
SEEDS_PATH = SRC_DIR / "hr_profanity_seeds.py"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

DIACRITICS = str.maketrans({"č": "c", "ć": "c", "đ": "d", "š": "s", "ž": "z"})

FALSE_POSITIVE = {
    "u", "i", "a", "o", "se", "je", "te", "me", "mi", "ti", "on", "ona", "od", "do", "na", "po",
    "za", "iz", "kod", "pa", "da", "ne", "ni", "no", "nu", "ga", "ju", "ih", "im", "si", "su",
    "rat", "ser", "sera", "kur", "kurir", "pick", "bum", "serija", "servis", "mongol", "download",
    "riba", "ribica", "jaje", "jaja", "kaka", "kakao", "dupe", "guz", "guzica", "stok", "goveda",
    "svinja", "debata", "idiom", "glava", "glavni", "rom", "frajer", "zena", "zenica",
}


def normalize(text: str) -> str:
    text = text.lower().translate(DIACRITICS)
    text = re.sub(r"[^a-z0-9]+", "", text)
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    return text.strip()


def load_seeds(path: Path) -> list[tuple[str, int, str, list[str], str]]:
    if not path.exists():
        return []
    ns: dict = {}
    exec(path.read_text(encoding="utf-8"), ns)  # noqa: S102
    return list(ns.get("SEEDS", []))


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def export_hr() -> dict:
    if not SRC_JSON.exists():
        raise SystemExit(
            f"Missing {SRC_JSON}. Run: python3 src/generate_hr_profanity_dataset.py"
        )

    data = json.loads(SRC_JSON.read_text(encoding="utf-8"))
    entries = data["entries"]

    words: set[str] = set()
    phrases: set[str] = set()
    normalized_words: set[str] = set()
    severity: dict[str, int] = {}

    def bump_severity(norm: str, sev: int) -> None:
        if not norm or norm in FALSE_POSITIVE:
            return
        severity[norm] = max(severity.get(norm, 0), sev)

    for entry in entries:
        if entry["severity"] < 2:
            continue
        variant = entry["variant"].strip().lower()
        if not variant or len(variant) < 2:
            continue
        norm = entry["normalized"]
        if len(norm) < 2 or norm in FALSE_POSITIVE:
            continue

        bump_severity(norm, int(entry["severity"]))

        if " " in variant:
            if not entry["obfuscated"]:
                phrases.add(variant)
            continue

        if entry["obfuscated"]:
            continue

        if len(variant) <= 48:
            words.add(variant)
        if len(norm) <= 48:
            normalized_words.add(norm)

    for lemma, sev, _cat, _loc, _kind in load_seeds(SEEDS_PATH):
        if sev < 2:
            continue
        lemma = lemma.strip().lower()
        if not lemma:
            continue
        n = normalize(lemma)
        bump_severity(n, sev)
        if " " in lemma:
            phrases.add(lemma)
        else:
            words.add(lemma)
            if n and n not in FALSE_POSITIVE:
                normalized_words.add(n)

    word_lines = sorted(words | {w for w in normalized_words if len(w) >= 2})
    phrase_lines = sorted(phrases)

    regex_src = json.loads(SRC_REGEX.read_text(encoding="utf-8")) if SRC_REGEX.exists() else {"patterns": []}
    patterns = regex_src.get("patterns", [])
    search_patterns = [
        {
            "root": p["root"],
            "pattern": p["pattern"],
            "severity": p["severity"],
            "category": p["category"],
            "normalized": normalize(p.get("root", "")),
        }
        for p in patterns
        if p.get("severity", 0) >= 2
    ][:4000]

    for row in search_patterns:
        norm = row.get("normalized") or ""
        if norm:
            bump_severity(norm, int(row["severity"]))

    return {
        "words": word_lines,
        "phrases": phrase_lines,
        "normalized": sorted(normalized_words),
        "regex": search_patterns,
        "severity": severity,
    }


def main() -> None:
    hr = export_hr()
    LISTS_DIR.mkdir(parents=True, exist_ok=True)

    write_lines(LISTS_DIR / "hr.txt", hr["words"])
    write_lines(LISTS_DIR / "hr-phrases.txt", hr["phrases"])
    write_lines(LISTS_DIR / "hr-normalized.txt", hr["normalized"])

    (LISTS_DIR / "hr-regex.json").write_text(
        json.dumps(
            {
                "meta": {
                    "language": "hr",
                    "purpose": "search_query_validation",
                    "pattern_count": len(hr["regex"]),
                    "flags": "iu",
                },
                "patterns": hr["regex"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (LISTS_DIR / "hr-severity.json").write_text(
        json.dumps(hr["severity"], ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"Croatian words: {len(hr['words'])}")
    print(f"Croatian phrases: {len(hr['phrases'])}")
    print(f"Croatian normalized: {len(hr['normalized'])}")
    print(f"Croatian regex: {len(hr['regex'])}")
    print(f"Croatian severity map: {len(hr['severity'])}")
    print(f"Output: {LISTS_DIR}")


if __name__ == "__main__":
    main()
