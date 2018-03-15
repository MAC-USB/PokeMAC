#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import curses
import time
import os

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
    os.system("timidity Title01.mid > /dev/null 2>/dev/null &")
    for i in range(0,numlineas+maxx):
        pantalla.refresh()
        pantalla.scroll(1)
        if lineas:
            linea = lineas.pop()
            linea = linea[:-1]
            pantalla.addstr(maxx-1, (maxy-1-linea.__len__())/2, linea)
        time.sleep(velocidad)
    os.system("killall timidity > /dev/null 2>/dev/null ")    
except KeyboardInterrupt:
    curses.endwin()
    os.system("killall timidity > /dev/null 2>/dev/null ")    

curses.endwin()


