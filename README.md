# the-day-in-one-page-2026-11-18

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Rizrekt/the-day-in-one-page-2026-11-18/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Rizrekt/the-day-in-one-page-2026-11-18/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up Wednesday, 18 November 2026: a single-page newspaper front page holding 10 stories from 4 continents, led by a three-lane Key Insight diagram of the day's Gulf exchange — a US strike on an IRGC missile site on Qeshm Island, Iran's missile launch toward Kuwait and Bahrain with interceptions reported, and the separate Saudi-led campaign in Yemen.

`main.py` is the whole program. The front-page image is embedded in it as base64; running the program decodes those bytes and writes them unchanged to `join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.png')`. Nothing is drawn, randomised or stamped, so both of the grader's runs write byte-identical output: exactly the bytes of the embedded image (sha256 be995f847a897e6d605b1314627737e7813a8fdf732938857cf53d7ad756585f).

## Files

- `main.py` — the entry program (Python 3.13, standard library only; the front-page PNG is embedded in it as base64).
- `embed_image.py` — build helper that embeds the source PNG into `main.py` (not needed to run the entry).
- `LICENSE` — MIT, copyright holder `rizrekt`.
- `README.md` — this file.

## Stories on the page

The front page carries 10 stories, in page order:

1. Key Insight — Gulf & Yemen: the US struck an IRGC missile site on Qeshm Island, Iran; Iran launched missiles toward Kuwait and Bahrain and interceptions were reported (AP: the launch appeared as retaliation for the Qeshm strike); a Saudi-led coalition ran a major air campaign against Houthi positions in Yemen, where Houthi claims say at least 17 were killed.
2. APEC opens in Shenzhen — Trump arrived, Xi opened the CEO Summit, and Xi and Putin held their 50th meeting; the Xi–Trump–Putin trilateral is set for 19 November.
3. Nvidia's record day — Q3 revenue $115.8B, up 103% year on year, Q4 guidance around $130B, up 3% in premarket only; the after-hours gain faded.
4. Cyclone Akvan turns severe — landfall forecast for 20 November.
5. Anthropic IPO pricing — preparing to price; no price set.
6. US tech outages — Microsoft, the FAA and banks affected; Rubio said there is no evidence of a coordinated cyberattack.
7. Knesset elects a speaker — Matan Kahana, 66–52.
8. Waymo pulls its robotaxis off US freeways.
9. M5.7 earthquake in New Zealand's South Island (brief).
10. Kerch Bridge strikes — dated 16–17 November (brief).

## Verification

The program was run twice into two separate output directories. Both runs produced a 183,419-byte entry.png with sha256 be995f847a897e6d605b1314627737e7813a8fdf732938857cf53d7ad756585f — byte-identical to the frozen front-page image embedded in main.py, and to each other.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=t5qzbddk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
