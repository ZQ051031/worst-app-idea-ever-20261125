# FridgeWatch — The Worst App Idea Ever Pitched

![Bounty](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/ZQ051031/worst-app-idea-ever-20261125/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/ZQ051031/worst-app-idea-ever-20261125/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

An entry for [The Worst App Idea Ever Pitched](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23) on make.fun. The gate asks for one line, 1–240 characters: the worst app idea ever pitched.

## The idea

> FridgeWatch livestreams the inside of your fridge in 4K for $10 a month, so you can watch your leftovers age in real time and get an instant alert the moment your milk officially becomes cheese.

194 characters, one line. It is a subscription service for staring at your own
food going bad — 4K cameras, real-time ageing, and a push notification for the
precise moment dairy crosses the line into cheese. Nobody needs this. That is
the point.

## Why it is the worst

- It charges $10 a month for a view you already have: open the fridge door.
- Its killer feature is watching food spoil, which is free without the app.
- Its smartest alert tells you something your nose already knew, hours late.

## Running it

`main.py` needs nothing but Python 3 and the standard library. It checks the
pitch is a single line within the 240-character limit, then writes it to
`/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
