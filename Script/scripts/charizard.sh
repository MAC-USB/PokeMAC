#!/bin/bash
cat /home/Entrenador/.poke_oculto/drawings/charizard.txt 
mplayer /home/Entrenador/.poke_oculto/sounds/charizard.mp3 >/dev/null 2>/dev/null

mkdir /home/Entrenador/johto/Monte_Plateado
mv /home/Entrenador/.poke_oculto/drawings/snorlax.txt /home/Entrenador/johto/Monte_Plateado
cd /home/Entrenador/johto/Monte_Plateado

chmod 555 /home/Entrenador/johto/Monte_Plateado/snorlax.txt