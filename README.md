# Croatian profanity list

**Content warning:** this repository contains vulgar, sexual, insulting, and
hate-related terms in Croatian and related South Slavic forms. It exists for
**content moderation, search filtering, and NLP safety** — not for harassment.

Open, MIT-licensed wordlists and a small Python pipeline to regenerate them.
Covers Croatian (`HR`) lemmas with regional overlap for `BA` / `RS` / `ME`.

## Live companion: Psovke

**Website:** [https://offshore.studio/psovke/](https://offshore.studio/psovke/)

[Psovke](https://offshore.studio/psovke/) (“Hall of Shame”) is a public
collector of Croatian curse words: submit a psovka, get a **brutometar** score
(0–100), vote on the rang lista, react, share, and roast. Strong community
submissions are meant to feed and stress-test this open dataset — for comedy
and for better moderation signals, not for harassing people.

| | |
|--|--|
| App | [offshore.studio/psovke](https://offshore.studio/psovke/) |
| Export API | [`/psovke/api/export`](https://offshore.studio/psovke/api/export) |
| About | [offshore.studio/psovke/about](https://offshore.studio/psovke/about) |

## Why this exists

Public English profanity lists are common; Croatian coverage is thin. This
project publishes curated seed lemmas plus expanded surface forms suitable for
blocking or flagging user-generated text (search queries, reviews, comments).
The Psovke site is the playful front door; this repo is the durable wordlist.

## Quick start (use the lists)

| File | Description | Approx. size |
|------|-------------|--------------|
| [`lists/hr.txt`](lists/hr.txt) | Surface lemmas / forms (one per line, UTF-8) | ~16k |
| [`lists/hr-phrases.txt`](lists/hr-phrases.txt) | Multi-word phrases | ~2k |
| [`lists/hr-normalized.txt`](lists/hr-normalized.txt) | Diacritic-folded / alphanumeric-normalized index | ~15k |
| [`lists/hr-severity.json`](lists/hr-severity.json) | Normalized term → severity `0–5` | — |
| [`lists/hr-regex.json`](lists/hr-regex.json) | Bypass-tolerant regex patterns | — |

Full generated dataset under [`data/`](data/): **CSV** (~740k rows), TXT, and
regex JSON are published. `profanity.json` is gitignored (exceeds GitHub’s
100 MB limit) — regenerate it locally with the generator below.

### Severity scale

| Score | Meaning |
|------:|---------|
| 0–1 | Mild / usually ignore |
| 2 | Mild insult |
| 3 | Strong insult / vulgar |
| 4 | Heavy sexual / slur-adjacent |
| 5 | Most severe |

Export scripts typically keep severity **≥ 2** for blocklists.

## Regenerate from seeds

Requires Python 3.10+.

```bash
cd croatian-profanity-list

# 1) Rebuild seed file from wordlists (optional; only if you edit wordlists)
python3 src/build_hr_profanity_seeds.py

# 2) Expand seeds → data/profanity.{json,csv,txt} + data/profanity.regex.json
python3 src/generate_hr_profanity_dataset.py

# 3) Export search-oriented lists into lists/
python3 src/export_hr_lists.py
```

Pipeline:

```
src/hr_profanity_wordlists.py
        ↓ build_hr_profanity_seeds.py
src/hr_profanity_seeds.py
        ↓ generate_hr_profanity_dataset.py
data/profanity.json (+ .csv, .txt, .regex.json)
        ↓ export_hr_lists.py
lists/hr*.txt / hr-*.json
```

## False positives

See [`tests/hr_false_positive_tests.txt`](tests/hr_false_positive_tests.txt) for
legitimate Croatian / product phrases that must **not** be blocked (e.g.
`kurir dostava`, `serija filmova`, `servis bicikla`). Matchers should use
word boundaries / allowlists accordingly.

## Intended use

- Search-query and UGC moderation
- Training / evaluating NLP filters
- Research on South Slavic offensive language
- Crowdsourced discovery via [Psovke](https://offshore.studio/psovke/) (vote-ranked candidates for list review)

**Not** for generating abuse, doxxing, or targeting protected groups.

## Credits

See [CREDITS.md](CREDITS.md). In particular, **148** Croatian terms were
merged from [LDNOOBW V2 `data/hr.txt`](https://github.com/LDNOOBWV2/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words_V2/blob/main/data/hr.txt)
(CC0) to fill gaps in our curated lists.

## License

[MIT](LICENSE) — © 2026 Ivan Miskic. Keep the copyright notice when
redistributing.

Upstream LDNOOBW V2 material remains under CC0 (public domain dedication);
attribution is still given in CREDITS for clarity.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
