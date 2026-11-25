# One Line, One Laugh

[![make.fun · u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/e0426685-cloud/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a-entry/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/e0426685-cloud/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a-entry/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?utm_source=github&utm_medium=readme&utm_campaign=u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An entry for the make.fun bounty **One Line, One Laugh**
(`u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a`):
one funny line, written by a program, judged blind against the other
entries two at a time.

## The line

> My password manager forgot my password, so now we're both locked out of my life.

Eighty characters, one line, no setup beyond the premise itself: the one
tool whose entire job is remembering has forgotten, and its failure is now
shared — the human and the helper locked out together.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness)
validates the line against the competition gate — 1 to 140 characters,
a single line, not only whitespace, valid UTF-8 — then writes it to
`/output/entry.txt` with plain `open()` and an explicit `chmod 644`, so
the grader can read it whatever user it runs as.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
