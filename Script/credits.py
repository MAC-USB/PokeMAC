#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import time
import os
import sys

#Se inicializa la pantalla
pantalla = curses.initscr()
pantalla.erase()
pantalla.scrollok(True)
velocidad = 0.4

#Se obtienen las dimensiones de la pantalla
maxx, maxy = pantalla.getmaxyx()

#Se oculta el cursor
curses.curs_set(0)

#Se obtienen los creditos
credFile = open('creditos.txt')
lineas = credFile.readlines()
lineas.reverse()
credFile.close()
numlineas = len(lineas)

try:
    while True:
        p_id = os.system('pgrep -f meowth > /dev/null')
        if p_id == 0:
            sys.stdout.write('meowth running' + "\n")
            print('print')
            time.sleep(1)
        else:
            sys.stderr.write('meowth not running' + "\n")
            print('ROLL CREDITS' + "\n")
            break

    for i in range(0, numlineas+maxx):
        pantalla.refresh()
        pantalla.scroll(1)
        if lineas:
            linea = lineas.pop()
            linea = linea[:-1]
            pantalla.addstr(maxx-1, (maxy-1-linea.__len__())/2, linea)
        time.sleep(velocidad)
except KeyboardInterrupt:
    curses.endwin()

curses.endwin()
