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


meowth_passwd = crypt.crypt('ayudame','22')
entrenador_passwd = crypt.crypt('YOTEELIJO','22')

os.system('useradd -s /bin/bash -p '+ meowth_passwd +' -m Meowth')
os.system('useradd -s /bin/bash -p '+ entrenador_passwd +' -m Entrenador')
print 'CREANDO USUARIO MEOWTH Y ENTRENADOR'


#Se crean los directorios castillos principales

os.system('mkdir -p /home/Entrenador/kanto/Bosque_Verde; chmod 755  /home/Entrenador/kanto/Bosque_Verde')
os.system('mkdir -p /home/Entrenador/kanto/Tunel_Roca; chmod 555 /home/Entrenador/kanto/Bosque_Verde')
os.system('mkdir -p /home/Entrenador/.poke_oculto/kanto/Tunel_Roca; chmod 777 /home/Entrenador/.poke_oculto/kanto/Tunel_Roca')
os.system('mkdir -p /home/Entrenador/.poke_oculto/johto/Islas_Remolino; chmod 777 /home/Entrenador/.poke_oculto/johto/Islas_Remolino')
os.system('mkdir -p /home/Entrenador/.poke_oculto/johto/Monte_Plateado; chmod 777 /home/Entrenador/.poke_oculto/johto/Monte_Plateado')

print 'CREANDO CARPETAS DE ZONAS'

#Asignacion de aliases 

# Preparando scripts y creditos
os.system('cp -r $(pwd)/scripts /home/Entrenador/.poke_oculto')
os.system('cp -r $(pwd)/credits /home/Entrenador/.poke_oculto')
os.system('cp -r $(pwd)/sounds /home/Entrenador/.poke_oculto')
os.system('cp -r $(pwd)/drawings /home/Entrenador/.poke_oculto')
os.system('cp -r $(pwd)/* /home/Meowth; chown -R Meowth:Meowth /home/Meowth')

os.system("echo \"cd /home/Entrenador/kanto/\" >> /home/Entrenador/.bashrc")
os.system("echo \"alias ls='ls --color'\" >> /home/Entrenador/.bashrc")
os.system("echo \"alias destello='/home/Entrenador/.poke_oculto/scripts/pikachu.sh'\" >> /home/Entrenador/.bashrc")
os.system("echo \"alias surf='source /home/Entrenador/.poke_oculto/scripts/blastoise.sh'\" >> /home/Entrenador/.bashrc")
os.system("echo \"alias vuelo='source /home/Entrenador/.poke_oculto/scripts/charizard.sh'\" >> /home/Entrenador/.bashrc")
os.system("echo \"alias pokeflauta='/home/Entrenador/.poke_oculto/scripts/snorlax.sh'\" >> /home/Entrenador/.bashrc")
os.system("echo \"alias instakillred='python /home/Entrenador/.poke_oculto/credits/credits.py'\" >> /home/Entrenador/.bashrc")

os.system("echo \"[[ -r ~/.bashrc  ]] && . ~/.bashrc\" >> /home/Entrenador/.bash_profile")

os.system('echo "" > /etc/motd')
os.system('echo "" > /var/run/motd.dynamic')

print 'ASIGNACION DE ALIASES y SUS RESPECTIVOS .bashrc'

# Pueblo Paleta

os.system('mkdir /home/Entrenador/kanto/Pueblo_Paleta; chmod 755 /home/Entrenador/kanto/Pueblo_Paleta')
os.system('touch /home/Entrenador/kanto/Pueblo_Paleta/.ditto')
os.system("echo \"Lo que buscas comienza con 159.90\" >> /home/Entrenador/kanto/Pueblo_Paleta/.ditto") #PRIMERA PARTE IP (CAT) XXX
CrearArchivo('/home/Entrenador/kanto/Pueblo_Paleta/grimer',100)
os.system("echo \"9.209\" >> /home/Entrenador/kanto/Pueblo_Paleta/grimer") #SEGUNDA PARTE IP (GREP) XXX.XXX
CrearArchivo('/home/Entrenador/kanto/Pueblo_Paleta/caterpie', 3000) #TERCERA PARTE IP XXX es el numero de lineas que es el num de ip XXX

print 'SE CREO PUEBLO PALETA'