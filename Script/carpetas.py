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

os.system('mkdir /home/Mario/Castillo_de_Kamek; chmod 755  /home/Mario/Castillo_de_Kamek')
os.system('mkdir /home/Mario/Castillo_de_KingBoo; chmod 700  /home/Mario/Castillo_de_KingBoo')
os.system('mkdir /home/Mario/Castillo_de_Bowser_jr; chmod 700  /home/Mario/Castillo_de_Bowser_jr')
os.system('mkdir /home/Mario/Castillo_de_Pirana_plant; chmod 700  /home/Mario/Castillo_de_Pirana_plant')

print 'CREANDO CARPETAS DE CASTILLOS'

#Asignacion de aliases 

os.system("echo \"alias destello='/home/meowth/scripts/pikachu.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias surf='/home/meowth/scripts/blastoise.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias vuelo='/home/meowth/scripts/charizard.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias pokeflauta='/home/meowth/scripts/snorlax.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias instakillred='python /home/invitado/admision/credits.py'\" >> /home/entrenador/.bashrc")
os.system('echo "" > /etc/motd')
os.system('echo "" > /var/run/motd.dynamic')

print 'ASIGNACION DE ALIASES y SUS RESPECTIVOS .bashrc'

###PUEBLO PALETA#####

os.system('mkdir /home/Mario/World; chmod 755 /home/Mario/World')
os.system('touch /home/Mario/World/.gombaa')
os.system("echo \"159.90\" >> /home/Mario/World/.gombaa") #PRIMERA PARTE IP (CAT) XXX
CrearArchivo('/home/Mario/World/jump',100)
os.system("echo \"9.199\" >> /home/Mario/World/jump") #SEGUNDA PARTE IP (GREP) XXX.XXX
CrearArchivo('/home/Mario/World/rock', 2019) #TERCERA PARTE IP XXX es el numero de lineas que es el num de ip XXX

print 'SE CREO EL MUNDO LIBRE'
