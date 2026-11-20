# The World Today — Thursday, 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/risman18/world-news-one-image-20261119-v3/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/risman18/world-news-one-image-20261119-v3/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the [make.fun bounty "Sum up 19 November's world news in one image"](https://make.fun/bounty/news-image-20261119) — $250 prize pool, top 50 share prizes.

## The image

A vintage navy-and-cream broadsheet front page, **"THE WORLD TODAY — Thursday, 19 November 2026"**, built from real news reported on 19 November 2026 (v3 full-day edition — the complete day, including the evening):

- **LEAD — Three at one table:** Trump, Xi and Putin meet in Shenzhen at APEC — their first trilateral meeting — and sign a four-point "Heads of State Declaration toward Peace" after 90 minutes. A nuclear war "cannot be won and must never be fought"; the declaration says nothing of Ukraine or Iran.
- **Genocide, the court rules:** The ICJ finds Myanmar committed genocide against the Rohingya in 2017 — the first state ever held responsible. Nine judges to six; reparations ordered.
- **Vice City's $2.36bn day:** GTA VI launches after 13 years — an estimated 24.6m copies sold on day one, about $2.36bn, the biggest entertainment launch on record (Sensor Tower).
- **The bridge hit again:** Third strike this week on the Crimean Bridge — the rail span is hit overnight and traffic halts.
- **A record $190.4M:** Van Gogh's *Blossoming Chestnut Trees* sets an artist record at Sotheby's after a Nazi-era ownership dispute is settled.
- **Also today:** Nvidia posts record $115.8bn revenue yet shares fall 2.9%; the US Senate rejects the Iran war-powers resolution 51–48; an ADNOC tanker is hit in the Hormuz attacks, 11 hurt, one missing; the EU proposes a €45bn loan for Ukraine; Cyclone Akvan nears India with 46,701 evacuated in Odisha; Voyager 1 is confirmed one light-day from Earth.

## How it works

`main.py` (Python 3, stdlib only) copies the pre-rendered `entry.png` — drawn at build time by `render_v3.py` (PIL + local fonts) with four hand-drawn illustrations — to `/output/entry.png`. The image is a deterministic 1024×1024 PNG (≤ 1 MiB). No network, no clock, no randomness — two runs produce byte-identical output.

```sh
python3 main.py        # writes /output/entry.png (or $MAKEFUN_OUTPUT_DIR)
```

## License

MIT — see [LICENSE](LICENSE).
