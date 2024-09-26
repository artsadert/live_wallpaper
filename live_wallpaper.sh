#!/bin/bash
path=~/programs/python/live_wallpaper/output
while true; do
  for d in $(ls $path); do
    for run in $(seq 30); do
      for x in $(ls $path/$d); do
        feh --bg-scale $path/$d/$x
        sleep 0.05
      done
    done
  done
done
