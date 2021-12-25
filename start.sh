#!/bin/bash
day=${2:-$(date +%d)}
year=${1:-$(date +%Y)}
mkdir -p $year/$day
cd $year/$day
aoc d -d $day -y $year
cp ../../solve.py .
aoc r -d $day -y $year > desc.md
