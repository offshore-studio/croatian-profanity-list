# Contributing

Thanks for helping improve Croatian moderation coverage.

## Ground rules

- This dataset is for **content moderation and safety research**.
- Do not open PRs that add personal data, real names, or targeted harassment lists.
- Prefer adding **lemmas** (dictionary forms) with severity + category; let the
  generators expand inflections and obfuscations.

## Add or fix terms

1. Edit [`src/hr_profanity_wordlists.py`](src/hr_profanity_wordlists.py) (base
   lists) **or** carefully extend [`src/hr_profanity_seeds.py`](src/hr_profanity_seeds.py).
2. Prefer regenerating seeds:

   ```bash
   python3 src/build_hr_profanity_seeds.py
   ```

3. Rebuild dataset + export lists:

   ```bash
   python3 src/generate_hr_profanity_dataset.py
   python3 src/export_hr_lists.py
   ```

4. Check [`tests/hr_false_positive_tests.txt`](tests/hr_false_positive_tests.txt).
   If a new pattern would block a legitimate query, add the query to that file
   and adjust false-positive / allowlist handling in the generators.

## Severity & categories

Use the severity scale in the README. Categories in seeds include e.g.
`sexual`, `excrement`, `insult`, `body_part`, `slur`, `family`, `religious`,
`violence`, `internet_slang`.

## Pull requests

- One logical change per PR (new lemmas **or** generator fix **or** docs).
- Include regenerated `lists/` (and `data/` if you ran the full generator) when
  the change affects published output.
- Describe why the term belongs (or why a false positive was fixed).
