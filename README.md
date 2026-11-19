# the-day-in-one-page-2026-11-18

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Rizrekt/the-day-in-one-page-2026-11-18/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Rizrekt/the-day-in-one-page-2026-11-18/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up Wednesday, 18 November 2026: a dense single-page newspaper front page holding 36 stories from 6 continents — 18 stories drawn in full (12 numbered stories plus 6 world briefs), a five-figure day-in-numbers strip, and 18 more stories in a one-line index — led by the Gulf exchange: a US strike on an IRGC missile site on Qeshm Island, Iran's missile launch toward Kuwait and Bahrain with interceptions reported, and the separate Saudi-led campaign in Yemen.

`main.py` is the whole program. The front-page image is embedded in it as base64; running the program decodes those bytes and writes them unchanged to `join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.png')`. Nothing is drawn, randomised or stamped, so both of the grader's runs write byte-identical output: exactly the bytes of the embedded image (264,340 bytes, sha256 2fa9324ac8a19397adbd9b23051e4f33e577f1c7d5a717d89922ee35baa67dd1).

## Files

- `main.py` — the entry program (Python 3.13, standard library only; the front-page PNG is embedded in it as base64).
- `embed_image.py` — build helper that embeds the source PNG into `main.py` (not needed to run the entry).
- `rewrap.py` — build helper that collapses the embedded payload onto a single line (not needed to run the entry).
- `LICENSE` — MIT, copyright holder `rizrekt`.
- `README.md` — this file.

## Stories on the page

The front page carries 36 stories, in page order:

1. The Gulf exchange — the US struck an IRGC missile site on Qeshm Island, Iran; Iran launched missiles toward Kuwait and Bahrain and interceptions were reported over both (AP: the launch appeared as retaliation for the Qeshm strike); on a separate front, a Saudi-led coalition flew a major air campaign against Houthi positions in Yemen, where a Houthi claim via AP says at least 17 were killed, and two Houthi cruise missiles were intercepted near Riyadh.
2. APEC opens in Shenzhen — Trump landed, Xi opened the CEO Summit and held a 50th meeting with Putin; the Xi–Trump–Putin trilateral is set for 19 November.
3. Nvidia's giant quarter — revenue $115.8B, up 103% year on year, EPS $2.68, Q4 guidance around $130B, up 3% in premarket only; the shadow side: the after-hours gain faded (briefly −0.3%), the chairman confirms Huang is not returning as CEO, and Asian shares fell in a "spy scandal".
4. Cyclone Akvan strengthens in the Bay of Bengal — now a severe cyclonic storm; forecast landfall around midday 20 November in Andhra Pradesh.
5. Outages hit Microsoft, the FAA and US banks — Secretary of State Rubio says there is no evidence of a coordinated cyberattack.
6. Anthropic prepares to price its IPO — pricing is being prepared; no price has been set.
7. Knesset elects Matan Kahana, 66–52 (Jerusalem Post).
8. Waymo pulls its robotaxis off US freeways (BBC).
9. Cyclone Xavier hits Category 5 near the northern Cook Islands (FBC News).
10. A California atmospheric river puts about 30 million people at flash-flood risk (ABC7).
11. M5.7 earthquake strikes New Zealand's South Island (1News).
12. Mongolia's president says he will resign — Khurelsukh cites abuse-of-power and bribery claims; parliament decides (Xinhua).
13. World brief — Fiji declares a disaster emergency over El Niño drought (RNZ).
14. World brief — Kerch Bridge arch down after strikes, dated 16–17 November; Kyiv calls it the final phase of a seven-stage operation.
15. World brief — PAHO revokes the measles-elimination status of the US, Mexico and Bolivia, dated 17 November.
16. World brief — Serbia's student protesters take seats in parliament, dated 17 November.
17. World brief — Protests against Prime Minister Fico erupt in Slovakia, dated 17 November.
18. World brief — DR Congo's Ebola outbreak passes 11,000 cases in total (cumulative), dated 17 November.
19. One-line index — UK benefits overhaul leads the papers (BBC).
20. One-line index — Haiti march backs Salvador troops (AFP; first reported 17 November).
21. One-line index — Mondlane on trial in Mozambique (AP; first reported 17 November).
22. One-line index — DR Congo: peace bids fail (Al Jazeera).
23. One-line index — Trump pulls FDA nominee Overton (CNBC).
24. One-line index — AI agent runs FX trade alone (CNBC; first reported 17 November).
25. One-line index — Lilly cancer deal to $5.9bn (Reuters; first reported 17 November).
26. One-line index — Afghanistan floods and hail kill 39 (first reported 17 November).
27. One-line index — US beat Haiti 2–0, into the Nations League semis (MLS; first reported 17 November).
28. One-line index — Rain and injury stall the Wanderers Test (ICC; first reported 17 November).
29. One-line index — Mo Abudu launches a $50m film fund (first reported 17 November).
30. One-line index — EU upholds African flight bans (first reported 17 November).
31. One-line index — EU to propose a €45bn loan for Ukraine (FT).
32. One-line index — North Korea tests a cluster warhead (KCNA).
33. One-line index — Dhoni ends his IPL playing career.
34. One-line index — Brazil: storms forecast in 16 states (G1).
35. One-line index — Northern France: orange flood alert (Le Figaro; first reported 17 November).
36. One-line index — Heavy rain downs Waikato trees (RNZ).

## Verification

The program was run into separate output directories across the build sessions. Every run produced a 264,340-byte entry.png with sha256 2fa9324ac8a19397adbd9b23051e4f33e577f1c7d5a717d89922ee35baa67dd1 — byte-identical to the frozen pola-juara front-page image embedded in main.py, and to each other.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=t5qzbddk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>