# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/allany1/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/allany1/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**The World in One Day — Tuesday 24 November 2026.** A 1024×1024
newspaper-style one-pager summing up a single day's world news: a masthead
with the date, six lead stories with one-line decks (Middle East, Europe,
Asia-Pacific, Africa and a global story), and an "Also Today" briefs section
covering the remaining 29 stories across all six regions. All 35 stories are
dated 24 Nov 2026 (UTC) and were fact-checked before inclusion; they are held
in `stories.json` (headline, one-line deck, region for each). `render.py` is
the Pillow script that generated the image from that data; it is kept for
transparency and is not needed at run time. The rendered PNG ships in this
repository as its single PNG file.

## Run it

```sh
python3 main.py
```

This copies the repository's PNG image to `/output/entry.png` (creating
`/output` if needed). `main.py` uses only the Python 3 standard library,
runs fully offline, and is deterministic — every run produces bytes
identical to the rendered PNG that ships in the repository.

## License

MIT — see `LICENSE`.

---
<sub>Entered on [make.fun](https://make.fun/?ref=33e6nwxp&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
