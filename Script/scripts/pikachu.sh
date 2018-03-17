#!/bin/bash
cat /home/Entrenador/.poke_oculto/drawings/pikachu.txt
mplayer /home/Entrenador/.poke_oculto/sounds/pikachu.mp3 >/dev/null 2>/dev/null

if [ $(pwd) == '/home/Entrenador/kanto/Tunel_Roca' ]
then
  mv /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/* /home/Entrenador/kanto/Tunel_Roca/
fi

chmod 555 /home/Entrenador/kanto/Tunel_Roca
chmod 000 /home/Entrenador/kanto/Tunel_Roca/medalla