# advent of code speedrunning repo
Mostly for personal use. Daily steps:
```sh
~/aoc$ . start.sh
...
~/aoc/YYYY/DD$ vi -s ../../start.vim
```
But before any of that, you will need to install the `aoc` package in this repo, by doing
```sh
~/aoc$ python3 -m pip install -e .
```

## Results
```
 22   00:03:50     21     80   01:35:17    845      0
 15   00:03:55     35     66   00:15:42    131      0
  9   00:02:50     40     61   00:06:22     10     91
  7   00:01:50     93      8   00:02:35     35     66
```
This library pays itself off _really, really_ well when a problem involves 2D grids/points.

It's also useful on almost every day for the `sread*` family of functions. But not much else.
