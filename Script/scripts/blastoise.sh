#!/bin/bash
cat /home/Entrenador/.poke_oculto/drawings/blastoise.txt 
mplayer /home/Entrenador/.poke_oculto/sounds/blastoise.mp3 >/dev/null 2>/dev/null

mkdir /home/Entrenador/johto
mv /home/Entrenador/.poke_oculto/johto/Islas_Remolino/ /home/Entrenador/johto/
cd /home/Entrenador/johto/Islas_Remolino

chmod 555 /home/Entrenador/johto/Islas_Remolino
chmod 755 /home/Entrenador/johto/Islas_Remolino/_under
chmod 500 /home/Entrenador/johto/Islas_Remolino/cOsA