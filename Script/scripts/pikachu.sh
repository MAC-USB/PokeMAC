#!/bin/bash
cat /home/meowth/drawings/pikachu.txt
mplayer /home/meowth/sounds/pikachu.mp3 >/dev/null 2>/dev/null

if [ $(pwd) == '/home/entrenador/kanto/tunel_roca' ]
then
  mv /home/meowth/.poke_oculto/kanto/tunel_roca/* /home/entrenador/kanto/tunel_roca/
fi
