#!/bin/bash
mplayer /home/meowth/sounds/pokeflute.mp3 >/dev/null 2>/dev/null

if [ $(pwd) == '/home/entrenador/johto/monte_plateado' ]
then
  mv /home/meowth/.poke_oculto/johto/monte_plateado/* /home/entrenador/johto/monte_plateado/
  rm snorlax.txt
fi
