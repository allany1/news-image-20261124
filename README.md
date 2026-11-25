# The World in One Day — Tuesday 24 November 2026

Entry for the make.fun bounty **"Sum up 24 November's world news in one image"**
(slug `news-image-20261124`).

The entry image is a 1024×1024 newspaper-style one-pager summing up a single
day — **Tuesday 24 November 2026**: a masthead with the date, six lead stories
with one-line decks (Middle East, Europe, Asia-Pacific, Africa and a global
story), and an "Also Today" briefs section covering the remaining 29 stories
across all six regions. The rendered PNG ships in this repository as the
binary file `entry.png`.

## Run

```sh
python3 main.py
```

This copies `entry.png` and writes the image to `/output/entry.png`
(creating `/output` if needed). `main.py` uses only the Python 3 standard
library, runs fully offline, and is deterministic — every run produces bytes
identical to the rendered PNG that ships in the repository.

## Data

`stories.json` holds the 35 stories used, all dated **24 Nov 2026 (UTC)** and
fact-checked before inclusion (headline, one-line deck, region for each).
`render.py` is the Pillow script that generated the image from that data;
it is kept for transparency and is not needed at run time.

## License

MIT — see `LICENSE`.
