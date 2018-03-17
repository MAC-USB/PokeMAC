#!/bin/bash
mplayer /home/Entrenador/.poke_oculto/sounds/pokeflute.mp3 >/dev/null 2>/dev/null

if [ $(pwd) == '/home/Entrenador/johto/Monte_Plateado' ]
then
 chmod 777 /home/Entrenador/johto/Monte_Plateado/snorlax.txt
 mv /home/Entrenador/.poke_oculto/johto/Monte_Plateado/* /home/Entrenador/johto/Monte_Plateado/
 rm /home/Entrenador/johto/Monte_Plateado/snorlax.txt
fi

chmod 755 /home/Entrenador/johto/Monte_Plateado
