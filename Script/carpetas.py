import itertools
import fileinput
import random
from random import randint
from random import choice
import os
import pwd
import crypt
import string
from string import lowercase
import sys

#FUNCIONES:

# Crea la ruta y le mete n archivos y n carpetas

#Se leen palabras de un diccionaro para crear las carpetas crap

f = open('/etc/dictionaries-common/words','r')

crap = f.readlines()
respaldo = crap
f.close()
random.shuffle(crap)

#Funcion que dado un numero, devuelve un numero aleatorio de n cifras
def random_N_digitos(n):
	rango_ini = 10**(n-1)
	rango_fin = (10**n)-1
	return randint(rango_ini, rango_fin)

def DirBasura(ruta, n):
	if not os.path.exists(ruta):
		os.mkdir(ruta)

	for i in range(int(n)):
		os.mkdir(ruta + '/' + crap.pop().strip() )
		archivo = open(ruta + '/' + crap.pop().strip() , 'w', 0)	

# Crea archivo con N lineas basura
def CrearArchivo(ruta, n,):
    archivo = open(ruta, 'w', 0)
    for i in range(int(n)):
        archivo.write(crap.pop().strip() + '\n')


toad_passwd = crypt.crypt('ayudame','22')
mario_passwd = crypt.crypt('MIQUIMI','22')

os.system('useradd -s /bin/bash -p '+ toad_passwd +' -m Toad')
os.system('useradd -s /bin/bash -p '+ mario_passwd +' -m Mario')
print 'CREANDO USUARIO TOAD Y MARIO'


#Se crean los directorios castillos principales

os.system('mkdir /home/entrenador/bosque_verde; chmod 755  /home/entrenador/bosque_verde')
os.system('mkdir /home/entrenador/tunel_roca; chmod 700  /home/entrenador/tunel_roca')
os.system('mkdir /home/entrenador/islas_remolinos; chmod 700  /home/entrenador/islas_remolinos')
os.system('mkdir /home/entrenador/monte_plateado; chmod 700  /home/entrenador/monte_plateado')

print 'CREANDO CARPETAS DE CASTILLOS'

#Asignacion de aliases 

os.system("echo \"alias mamamia='su'\" >> /home/Mario/.bashrc")
os.system("echo \"alias ls='ls --color'\" >> /home/Mario/.bashrc")
os.system("echo \"alias instakillbowser='python /home/invitado/admision/credits.py'\" >> /home/Mario/.bashrc")
os.system('echo "" > /etc/motd')
os.system('echo "" > /var/run/motd.dynamic')

print 'ASIGNACION DE ALIASES y SUS RESPECTIVOS .bashrc'

###PUEBLO PALETA#####

os.system('mkdir /home/entrenador/pueblo_paleta; chmod 755 /home/Mario/World')
os.system('touch /home/entrenador/pueblo_paleta/.gombaa')
os.system("echo \"159.90\" >> /home/entrenador/pueblo_paleta/.gombaa") #PRIMERA PARTE IP (CAT) XXX
CrearArchivo('/home/entrenador/pueblo_paleta/jump',100)
os.system("echo \"9.199\" >> /home/entrenador/pueblo_paleta/jump") #SEGUNDA PARTE IP (GREP) XXX.XXX
CrearArchivo('/home/entrenador/pueblo_paleta/rock', 2019) #TERCERA PARTE IP XXX es el numero de lineas que es el num de ip XXX

print 'SE CREO EL MUNDO LIBRE'