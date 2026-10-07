#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build expanded seed list and write hr_profanity_seeds.py."""

from pathlib import Path
import sys

_SRC = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from hr_profanity_wordlists import (
    ADJ,
    BASE_VERBS,
    BODY_TARGETS,
    FAMILY_TARGETS,
    INSULT_NOUNS,
    INSULT_SUFFIX_F,
    INSULT_SUFFIX_M,
    INSULT_SUFFIX_N,
    INTERNET,
    NOUN_F,
    NOUN_HR,
    NOUN_M,
    PREFIXES,
    REGIONAL_BA_RS,
    SLURS,
    STEMS_FOR_SUFFIX,
    STEMS_SUFFIX,
    SUFFIXES,
    VERB_ATI,
    VERB_ATI_HR,
    VERB_IMP,
)

ALL = ["HR", "BA", "RS", "ME"]
HR = ["HR"]
BA_RS = ["BA", "RS"]


def s(lemma, severity, category, locales=None, kind="noun_m"):
    return (lemma, severity, category, tuple(locales or ALL), kind)


def infer_kind(word: str, default: str = "noun_m") -> str:
    if word.endswith("ati") or word.endswith("iti"):
        return "verb_ati"
    if word.endswith("a") and not word.endswith("acija"):
        return "noun_f"
    if default:
        return default
    return "noun_m"


def add_compounds(seeds: list) -> None:
    for target in FAMILY_TARGETS:
        for tmpl, sev in [
            (f"jebem ti {target}", 5),
            (f"jebem mu {target}", 5),
            (f"jebem vam {target}", 5),
            (f"jebem im {target}", 5),
            (f"jebem li ti {target}", 5),
            (f"mater ti jebem {target}", 5),
            (f"jebo ti {target}", 5),
            (f"jebo mu {target}", 5),
            (f"jebo vam {target}", 5),
            (f"jebo im {target}", 5),
            (f"proklet bio tvoj {target}", 4),
            (f"prokleta ti {target}", 4),
        ]:
            if target in tmpl or tmpl.endswith(target):
                seeds.append(s(tmpl, sev, "family", kind="expression"))

    for body in BODY_TARGETS:
        for tmpl, sev, cat in [
            (f"u {body}", 4, "sexual"),
            (f"idi u {body}", 4, "insult"),
            (f"odi u {body}", 4, "insult"),
            (f"boli me {body}", 3, "sexual"),
            (f"puši {body}", 4, "sexual"),
            (f"pusi {body}", 4, "sexual"),
            (f"gutaj {body}", 4, "sexual"),
            (f"polizi {body}", 4, "sexual"),
            (f"u {body} materinu", 5, "family"),
            (f"{body} ti", 4, "insult"),
            (f"{body} ti materina", 5, "family"),
            (f"koji {body}", 3, "insult"),
            (f"koja {body}", 3, "insult"),
            (f"sta je {body}", 3, "insult"),
            (f"sta je ovo {body}", 3, "insult"),
            (f"puni usta {body}", 4, "excrement"),
        ]:
            seeds.append(s(tmpl, sev, cat, kind="expression"))

    for verb in VERB_IMP:
        for tmpl, sev in [
            (f"{verb} se", 5),
            (f"{verb} ga", 4),
            (f"{verb} je", 4),
            (f"{verb} ih", 4),
            (f"{verb} me", 4),
            (f"{verb} nas", 4),
            (f"{verb} vas", 4),
            (f"{verb} odavde", 5),
            (f"{verb} od mene", 5),
        ]:
            seeds.append(s(tmpl, sev, "sexual", kind="expression"))

    for noun in INSULT_NOUNS:
        seeds.append(s(f"{noun} si", 3, "insult", kind="expression"))
        seeds.append(s(f"nisi {noun}", 3, "insult", kind="expression"))
        seeds.append(s(f"ti si {noun}", 3, "insult", kind="expression"))
        seeds.append(s(f"pravi {noun}", 3, "insult", kind="expression"))
        seeds.append(s(f"totalni {noun}", 3, "insult", kind="expression"))
        seeds.append(s(f"pravi {noun}", 3, "insult", kind="expression"))
        for suf in INSULT_SUFFIX_M:
            seeds.append(s(f"{noun} {suf}", 3, "insult", kind="expression"))
        for suf in INSULT_SUFFIX_F:
            seeds.append(s(f"{noun} {suf}", 3, "insult", kind="expression"))

    religious = [
        ("jebo te bog", 5), ("jebo te vrag", 4), ("jebo te pas", 4), ("jebo te crkva", 4),
        ("bog te jebo", 4), ("vrag te jebo", 4), ("pakao te jebo", 4), ("krst te jebo", 4),
        ("crkva ti materina", 4), ("jebote", 4), ("jebiga", 4), ("jebiga bre", 4),
        ("jebote u usta", 5), ("jebote sunce", 4), ("jebote more", 4), ("jebote zemlja", 4),
        ("proklet bio", 4), ("prokleta budi", 4), ("proklet bio tvoj", 4), ("proklet bio ti", 4),
        ("u tri pm", 3), ("do vraga", 3), ("u pakao", 4), ("idi u pakao", 4),
        ("jebem ti sunce", 4), ("jebem ti vjere", 5), ("jebem ti crkvu", 5),
        ("jebem ti krv", 5), ("jebem ti kosti", 5), ("jebem ti dušu", 5),
        ("jebem ti dušu", 5), ("jebem ti dušu", 5),
    ]
    for phrase, sev in religious:
        seeds.append(s(phrase, sev, "religious", kind="expression"))

    violence = [
        ("ubij se", 4), ("ubij ga", 4), ("ubij je", 4), ("ubij ih", 4), ("ubij me", 4),
        ("prebij ga", 4), ("prebij je", 4), ("prebij ih", 4), ("tuci ga", 4), ("tuci je", 4),
        ("tuci ih", 4), ("mlati ga", 4), ("mlati je", 4), ("mlati ih", 4),
        ("izmasi ga", 4), ("izmasi je", 4), ("izmasi ih", 4), ("izmasi me", 4),
        ("polomi ga", 4), ("polomi je", 4), ("polomi ih", 4), ("usmrti ga", 5),
        ("usmrti je", 5), ("usmrti ih", 5), ("zadavim te", 5), ("zadavim ga", 5),
        ("guzim te", 4), ("guzim ga", 4), ("guzim je", 4), ("guzim ih", 4),
        ("nacupam ti", 4), ("nacupam ga", 4), ("nacupam je", 4), ("nacupam ih", 4),
    ]
    for phrase, sev in violence:
        seeds.append(s(phrase, sev, "violence", kind="expression"))

    gaming = [
        ("noob", 1), ("nub", 1), ("scrub", 1), ("rekt", 1), ("pwned", 1), ("owned", 1),
        ("ez", 1), ("trash", 2), ("garbage", 2), ("camper", 1), ("camperu", 1),
        ("toxic", 2), ("toxicu", 2), ("reportaj ga", 1), ("reportaj je", 1),
        ("lag", 1), ("lagger", 1), ("cheater", 2), ("cheateru", 2), ("hacker", 2),
        ("hackeru", 2), ("smurf", 1), ("boosted", 1), ("inting", 2), ("feeder", 2),
        ("feederu", 2), ("grief", 2), ("griefer", 2), ("grieferu", 2),
    ]
    for phrase, sev in gaming:
        seeds.append(s(phrase, sev, "internet_slang", kind="expression"))

    extra = [
        ("jebem ti mater", 5, "family"), ("mater ti jebem", 5, "family"),
        ("picka ti materina", 5, "family"), ("pizda ti materina", 5, "family"),
        ("kurac ti u usta", 5, "sexual"), ("u usta ti kurac", 5, "sexual"),
        ("guzica ti materina", 4, "family"), ("mater ti", 4, "family"), ("oca ti", 4, "family"),
        ("sestru ti", 4, "family"), ("familiju ti", 4, "family"), ("baba ti", 4, "family"),
        ("deda ti", 4, "family"), ("pizda materina", 5, "family"), ("picka materina", 5, "family"),
        ("kurac palac", 3, "insult"), ("jebem ti", 5, "family"), ("jebem li ti", 5, "family"),
        ("jebemu mater", 5, "family"), ("jebem mu mater", 5, "family"), ("jebem vam mater", 5, "family"),
        ("jebem vam oca", 5, "family"), ("jebem mu oca", 5, "family"), ("jebem mu familiju", 5, "family"),
        ("jebem ti djecu", 5, "family"), ("jebem ti zenu", 5, "family"), ("jebem ti baku", 5, "family"),
        ("jebem ti dedu", 5, "family"), ("jebem ti roditelje", 5, "family"), ("jebem ti sestru", 5, "family"),
        ("jebem ti oca", 5, "family"), ("jebem ti familiju", 5, "family"),
        ("smrdi na govno", 3, "excrement"), ("smrdi na sranje", 3, "excrement"),
        ("puni usta govna", 4, "excrement"), ("puni usta sranja", 4, "excrement"),
        ("puni usta", 3, "sexual"), ("gltaj kurac", 5, "sexual"), ("gutaj kurac", 5, "sexual"),
        ("pederu jedan", 5, "homophobic"), ("pederu glupi", 5, "homophobic"),
        ("pederu smrdljivi", 5, "homophobic"), ("retardu", 4, "ableist"),
        ("debilu jedan", 3, "insult"), ("kretenu jedan", 3, "insult"), ("idiote jedan", 2, "insult"),
        ("budalo jedna", 2, "insult"), ("droljo jedna", 4, "sexual"), ("kurvo jedna", 4, "sexual"),
        ("pizdo jedna", 5, "body_part"), ("picko jedna", 5, "body_part"), ("seronjo jedan", 3, "insult"),
        ("govedo jedno", 3, "insult"), ("svinjo jedna", 3, "insult"), ("stoko jedna", 3, "insult"),
        ("glupan jedan", 2, "insult"), ("glupane", 2, "insult"), ("sta je kurac", 3, "insult"),
        ("sta je picka", 3, "insult"), ("guzica ti", 3, "family"),
        ("pickin sin", 5, "family"), ("pizdin sin", 5, "family"), ("kurvin sin", 4, "family"),
        ("sin pickin", 5, "family"), ("sin pizdin", 5, "family"), ("sin kurvin", 4, "family"),
        ("kcer picka", 5, "family"), ("kcer pizda", 5, "family"), ("kcer kurva", 4, "family"),
    ]
    for item in extra:
        if len(item) == 3:
            seeds.append(s(item[0], item[1], item[2], kind="expression"))
        else:
            seeds.append(s(item[0], item[1], "insult", kind="expression"))


def main():
    seeds: list = []

    for word, sev, cat in VERB_ATI:
        seeds.append(s(word, sev, cat, kind="verb_ati"))

    for word, sev, cat in VERB_ATI_HR:
        seeds.append(s(word, sev, cat, HR, "verb_ati"))

    for word, sev, cat in NOUN_M:
        seeds.append(s(word, sev, cat, kind="noun_m"))

    for word, sev, cat in NOUN_F:
        seeds.append(s(word, sev, cat, kind="noun_f"))

    for word, sev, cat in NOUN_HR:
        kind = infer_kind(word, "noun_m")
        seeds.append(s(word, sev, cat, HR, kind))

    for word, sev, cat in SLURS:
        seeds.append(s(word, sev, cat, kind="slur"))

    for word, sev, cat in ADJ:
        seeds.append(s(word, sev, cat, kind="adj"))

    for word, sev, cat in INTERNET:
        seeds.append(s(word, sev, cat, kind="expression"))

    for word, sev, cat in REGIONAL_BA_RS:
        seeds.append(s(word, sev, cat, BA_RS + ["ME"], "expression"))

    for p in PREFIXES:
        for b in BASE_VERBS:
            w = p + b
            if w != b:
                cat = "sexual" if "jeb" in w else "excrement" if "ser" in w or "sra" in w else "sexual"
                seeds.append(s(w, 4, cat, kind="verb_ati"))

    for stem, sev, cat in STEMS_SUFFIX:
        for suf in SUFFIXES:
            w = stem + suf
            kind = "noun_f" if suf in {"ica", "ina", "cina", "cuga", "usa"} else "noun_m"
            seeds.append(s(w, sev, cat, kind=kind))

    for stem, sev, cat in STEMS_FOR_SUFFIX:
        for suf in INSULT_SUFFIX_M + INSULT_SUFFIX_F + INSULT_SUFFIX_N:
            w = f"{stem} {suf}"
            seeds.append(s(w, sev, cat, kind="expression"))

    add_compounds(seeds)

    # Deduplicate
    seen = set()
    unique = []
    for item in seeds:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    out = Path(__file__).with_name("hr_profanity_seeds.py")
    lines = [
        "# -*- coding: utf-8 -*-",
        '"""Profanity seed lemmas for Croatian moderation dataset."""',
        "",
        "SEEDS = [",
    ]
    for lemma, severity, category, locales, kind in unique:
        loc = ", ".join(f'"{x}"' for x in locales)
        lines.append(f'    ("{lemma}", {severity}, "{category}", [{loc}], "{kind}"),')
    lines.append("]")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(unique)} seeds to {out}")


if __name__ == "__main__":
    main()
