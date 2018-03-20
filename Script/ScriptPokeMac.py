#!/usr/bin/python

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

######################## CONSTRUCCION ZONAS ########################################################################

################################
# ZONA NUMERO 1 (Bosque_Verde) #
################################



#Garantizo que no existan las siguientes carpetas y luego las creo

os.system('find /home/Entrenador/kanto/Bosque_Verde -name _ATK | xargs rm -rf')
os.system('find /home/Entrenador/kanto/Bosque_Verde -name _DEF | xargs rm -rf')
os.system('find /home/Entrenador/kanto/Bosque_Verde -name POKE | xargs rm -rf')

os.system('mkdir -p /home/Entrenador/kanto/Bosque_Verde/_ATK/_LVL')
os.system('mkdir -p /home/Entrenador/kanto/Bosque_Verde/_DEF/_HP')
os.system('touch /home/Entrenador/kanto/Bosque_Verde/_ATK/##PONME_TODO')
os.system('touch /home/Entrenador/kanto/Bosque_Verde/_ATK/_LVL/##ESO_PA_LANTE')
os.system('touch /home/Entrenador/kanto/Bosque_Verde/_DEF/##PONME_TODO')
os.system('touch /home/Entrenador/kanto/Bosque_Verde/_DEF/_HP/##ESO_PA_LANTE')

os.system('touch /home/Entrenador/kanto/Bosque_Verde/POKE')
os.system('touch /home/Entrenador/kanto/Bosque_Verde/trueno')
lineas = respaldo

#Creo el contenido del archivo POKE para su pregunta

for i in range(50):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> /home/Entrenador/kanto/Bosque_Verde/POKE')

for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(45))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >> /home/Entrenador/kanto/Bosque_Verde/POKE')
os.system('echo ":5432accb se_te_acaba_el_tiempo" >> /home/Entrenador/kanto/Bosque_Verde/POKE')
for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(30))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')
os.system('echo ":1322eccb acabas_de_conseguir_la_clave_nxt" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')
for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(34))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')
for i in range(307):
	str0 = "".join(choice(lowercase) for j in range(24))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')
os.system('echo ":1352eccba a_Meowth_le_gustan_las_galletas" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')
for i in range(300):
	str0 = "".join(choice(lowercase) for j in range(27))
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')
for i in range(50):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >>  /home/Entrenador/kanto/Bosque_Verde/POKE')

print " --SE CARGO EL BOSQUE VERDE"
DirBasura("/home/Entrenador/kanto/Bosque_Verde" , 800)
#Fin del CASTILLO DE KAMEK

######################## Fin del BOSQUE VERDE ########################################################################

##############################
# ZONA NUMERO 2 (Tunel_Roca) #
##############################

os.system('rm -rf /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medium')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medium')
for i in range(99):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >>  /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medium')
os.system('echo equlilibrio >>  /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medium')     #Essta es la linea del medio
for i in range(100):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >>  /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medium')

os.system('rm -rf /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medalla') 
os.system('cp /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medium /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medalla')
os.system('chmod 000 /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medalla ; chown Entrenador:Entrenador /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/medalla') 


#Cosas de la pregunta 7
masks=['oak','centro','bill','mimo','lago','pokiman','nintendo', 'ho-oh',\
           'geodude','rattata', 'pidgey', 'caterpie']

words_from_masks = []
for i in range(1,300):
    for m in masks:	
        num = i % 5
        if num != 0:
            words_from_masks.append(m + str(random_N_digitos(int(num))))

words_from_masks = list(set(words_from_masks))
respaldo_wfms = words_from_masks

#Archivo en el que deberan mostrar el contenido de los archivos que esten
#contenidos en el 

os.system('rm -rf /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/golpe')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/golpe')

for w in words_from_masks:
	os.system('echo '+ w + ' >> /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/golpe')	
os.system('echo master_ball >> /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/golpe')
for i in range(800):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/golpe')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/master_ball')
os.system('echo "hidro" >> /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/master_ball')


#_Pipe pregunta (12)

os.system('rm -rf /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada')
os.system('mkdir -p /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada')
jigglypuff='pika'
jigglypuff_l = map(''.join, itertools.product(*zip(jigglypuff.upper(), jigglypuff.lower())))
dir_jigglypuff = ['_THE','_LEGEND','_OF','_SUPER','_MAC','_BROS']

for z in jigglypuff_l:  #Se mina todo el directorio _CASCADA (nivel 1)
	os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/'+z) 
for z in dir_jigglypuff:
	os.system('mkdir -p /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/'+z)	
	for a in jigglypuff_l:  #Se minan todos los directorios del segundo nivel
		os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/'+z+'/'+a) 
	for x in dir_jigglypuff:
		os.system('mkdir -p /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/'+z+'/'+x)	
		for y in dir_jigglypuff:
			os.system('mkdir -p /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/'+z+'/'+x+'/'+y)	
			for a in jigglypuff_l:  #Se minan todos los directorios del cuarto nivel
				os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/'+z+'/'+x+'/'+y+'/'+a)

os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/_THE/_LEGEND/Pika')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/_OF/_THE/pIKa')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/_SUPER/_MAC/pikA')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_Cascada/_BROS/_BROS/PikA')

#carpetas que comienzen con - para la pregunta (11)

os.system('mkdir -p  /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_MGKRP')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/_MGKRP/-gary')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-gary')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-EAS')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-is')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-the')
os.system('mkdir -p /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-HERO')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-HERO/-of')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-HERO/-this')
os.system('touch /home/Entrenador/.poke_oculto/kanto/Tunel_Roca/-HERO/-world')

DirBasura('/home/Entrenador/.poke_oculto/kanto/Tunel_Roca' , 800)
print " --SE CARGO EL TUNEL ROCA"

######################## Fin del CASTILLO DE KINGBOO ########################################################################

##################################
# ZONA NUMERO 3 (Islas_Remolino) #
##################################

# Pregunta N 14
# Garantizo que este la carpeta y le agrego lo que necesito
os.system('mkdir /home/Entrenador/.poke_oculto/johto/Islas_Remolino/_under')
os.system('touch /home/Entrenador/.poke_oculto/johto/Islas_Remolino/_under/lugia')

# Pregunta N 17
# Genera un archivo cOsA con permisos 700 y luego una carpera _kart con permisos 777
os.system('touch /home/Entrenador/.poke_oculto/johto/Islas_Remolino/cOsA && chmod 700 /home/Entrenador/.poke_oculto/johto/Islas_Remolino/cOsA')
os.system('mkdir /home/Entrenador/.poke_oculto/johto/Islas_Remolino/_ball')

aux = respaldo_wfms
aux1 = respaldo_wfms
aux2 = respaldo_wfms

for i in range(50):
    os.system('touch /home/Entrenador/.poke_oculto/johto/Islas_Remolino/_ball/' + aux.pop())


for i in range (10):
    os.system('touch /home/Entrenador/.poke_oculto/johto/Islas_Remolino/_under/' + aux1.pop()[:4])
    os.system('touch /home/Entrenador/.poke_oculto/johto/Islas_Remolino/_under/' + aux2.pop()[:6])

print "---SE CARGO LAS ISLAS REMOLINO"
DirBasura('/home/Entrenador/.poke_oculto/johto/Islas_Remolino' , 800)

######################## Fin del CASTILLO DE BOWSER JR. ########################################################################


##################################
# ZONA NUMERO 4 (Monte_Plateado) #
##################################

os.system('rm -rf /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Grass')
os.system('rm -rf /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Region')
lineas = respaldo
os.system('mkdir /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Grass')
os.system('mkdir /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Region')
for i in range(800):
	os.system('touch /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Grass/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))
for i in range(600):
	os.system('touch /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Region/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))

os.system('cp -r /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Grass/ /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Grass2')
os.system('cp -r /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Region/ /home/Entrenador/.poke_oculto/johto/Monte_Plateado/_Region2')
	

#archivo random que tendra 30 lineas
os.system('rm -rf /home/Entrenador/.poke_oculto/johto/Monte_Plateado/gyarados')
os.system('touch /home/Entrenador/.poke_oculto/johto/Monte_Plateado/gyarados')
for i in range(30):
    os.system("echo Super EAS Odyssey >> /home/Entrenador/.poke_oculto/johto/Monte_Plateado/gyarados")

#Colocandole 30K a un archivo
os.system('mkdir -p /home/Entrenador/.poke_oculto/johto/Monte_Plateado/BOSS/RED/IS/IN/HIS/')
os.system('touch /home/Entrenador/.poke_oculto/johto/Monte_Plateado/BOSS/RED/IS/IN/HIS/riegame')
for i in range(9999):
    os.system("echo aa >> /home/Entrenador/.poke_oculto/johto/Monte_Plateado/BOSS/RED/IS/IN/HIS/riegame")
os.system('echo "CREETE QUE ERES SUPER EAS... DI EN VOZ ALTA: SOY EAS" >> /home/Entrenador/.poke_oculto/johto/Monte_Plateado/BOSS/RED/IS/IN/HIS/riegame')


os.system('rm -rf /home/Entrenador/.poke_oculto/johto/Monte_Plateado/eevee-saur')
os.system('rm -rf /home/Entrenador/.poke_oculto/johto/Monte_Plateado/ivy-saur')

os.system('touch /home/Entrenador/.poke_oculto/johto/Monte_Plateado/eevee-saur')
os.system('touch /home/Entrenador/.poke_oculto/johto/Monte_Plateado/ivy-saur')

words_from_masks = respaldo_wfms
for w in words_from_masks:
    	os.system('echo '+ w + '>> /home/Entrenador/.poke_oculto/johto/Monte_Plateado/eevee-saur')

palabra_distinta= 'r3D'
aux = words_from_masks + [palabra_distinta]

random.shuffle(aux)        
for w in aux:
    	os.system('echo '+ w + '>> /home/Entrenador/.poke_oculto/johto/Monte_Plateado/ivy-saur')



print '---SE CARGO EL MONTE PLATEADO'
DirBasura('/home/Entrenador/.poke_oculto/johto/Monte_Plateado/' , 800)

os.system('chown Entrenador:Entrenador /home/Entrenador/kanto')
os.system('chown -R Entrenador:Entrenador /home/Entrenador/.poke_oculto')
os.system('chown Entrenador:Entrenador /home/Entrenador/')
os.system('chown Entrenador:Entrenador /home/Entrenador/kanto/Tunel_Roca')

#Fin del Castillo_de_Pirana_plant
######################## Fin del CASTILLO DE PIRANA_PLANT ###################################################################
