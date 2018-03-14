#!/usr/bin/python

import itertools
import os
import sys
from random import choice, randint, shuffle
from string import lowercase

# FUNCTIONS

f = open('/etc/dictionaries-common/words', 'r')

crap = f.readlines()
respaldo = crap
f.close()
shuffle(crap)

# Given a number, returns a random number of n digits
def random_N_digitos(n):
	range_ini = 10**(n-1)
	range_fin = (10**n)-1
	return randint(range_ini, range_fin)

def DirBasura(path, n):
	if not os.path.exists(path):
		os.mkdir(path)

	for i in range(int(n)):
		os.mkdir(path + '/' + crap.pop().strip() )
		archivo = open(path + '/' + crap.pop().strip() , 'w', 0)

# Create a file and fill it with n lines of random data
def create_file(path, n):
    with open(path, 'w') as f:
        for i in range(int(n)):
            f.write(crap.pop().strip() + '\n')


########################
# ZONE 0 - pueblo_paleta
########################

# 1
with open('/home/entrenador/kanto/pueblo_paleta/.ditto', 'a') as f:
    f.write('Lo que buscas comienza con 159.90') # TODO

# 2
create_file('/home/entrenador/kanto/pueblo_paleta/grimer', 100)
with open('/home/entrenador/kanto/pueblo_paleta/grimer', 'a') as f:
    f.write('9.199') # TODO

# 3
create_file('/home/entrenador/kanto/pueblo_paleta/caterpie', 2019) # TODO


#######################
# ZONE 1 - bosque_verde
#######################

# CHALLENGE 2 / 4
# Guarantee that the dirs do not exist.
os.system('find /home/entrenador/kanto/bosque_verde -name _ATK | xargs rm -rf')
os.system('find /home/entrenador/kanto/bosque_verde -name _DEF | xargs rm -rf')

# Now create them
os.system('mkdir -p /home/entrenador/kanto/bosque_verde/_ATK/_LVL')
os.system('mkdir -p /home/entrenador/kanto/bosque_verde/_DEF/_HP')
os.system('touch /home/entrenador/kanto/bosque_verde/{_ATK,_DEF}/##PONME_TODO')
os.system('touch /home/entrenador/kanto/bosque_verde/{_ATK/_LVL,_DEF/_HP}/##ESO_PA_LANTE')

# CHALLENGE 5
os.system('find /home/entrenador/kanto/bosque_verde -name POKE | xargs rm -rf')
os.system('touch /home/entrenador/kanto/bosque_verde/POKE')
lineas = respaldo

# Fill the file POKE
for i in range(50):
	os.system('echo "' + (((lineas.pop()).lower()).replace("'",":")).strip("\n") + '" >> /home/entrenador/kanto/bosque_verde/POKE')
for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(45))
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >> /home/entrenador/kanto/bosque_verde/POKE')
os.system('echo ":5432accb se_te_acaba_el_tiempo_menor" >> /home/entrenador/kanto/bosque_verde/POKE')
for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(30))
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >> /home/entrenador/kanto/bosque_verde/POKE')
os.system('echo ":1322eccb acabas_de_conseguir_la_clave_babe" >> /home/entrenador/kanto/bosque_verde/POKE')
for i in range(207):
	str0 = "".join(choice(lowercase) for j in range(34))
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >> /home/entrenador/kanto/bosque_verde/POKE')
for i in range(307):
	str0 = "".join(choice(lowercase) for j in range(24))
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >> /home/entrenador/kanto/bosque_verde/POKE')
os.system('echo ":1352eccba Meowth_dice_que_la_clave_es_nxt" >> /home/entrenador/kanto/bosque_verde/POKE')
for i in range(300):
	str0 = "".join(choice(lowercase) for j in range(27))
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >>  /home/entrenador/kanto/bosque_verde/POKE')
for i in range(50):
	os.system('echo "' + (((lineas.pop()).lower()).replace("'",":")).strip("\n") + '" >>  /home/entrenador/kanto/bosque_verde/POKE')

DirBasura("/home/entrenador/kanto/bosque_verde" , 800)


#####################
# ZONE 2 - tunel_roca
#####################

# CHALLENGE 8
os.system('rm -rf /home/entrenador/kanto/tunel_roca/medium')
os.system('touch /home/entrenador/kanto/tunel_roca/medium')

# Deprecated. Remove on verification.
# for i in range(99):
# 	str0 = "".join(choice(lowercase) for j in range(6))
# 	os.system('echo ' + str0 + ' >> /home/entrenador/kanto/tunel_roca/medium')

with open('/home/entrenador/kanto/tunel_roca/medium', 'a') as f:

    for i in range(99):
        random_string = "".join(choice(lowercase) for j in range(6))
        f.write(random_string)

    # Middle line
    f.write('equilibrio')

    for i in range(100):
        random_string = "".join(choice(lowercase) for j in range(6))
        f.write(random_string)

# Deprecated. Remove on verification.
# for i in range(100):
# 	str0 = "".join(choice(lowercase) for j in range(6))
# 	os.system('echo ' + str0 + ' >> /home/entrenador/kanto/tunel_roca/medium')

# CHALLENGE 9
os.system('rm -rf /home/entrenador/kanto/tunel_roca/medalla')
os.system('cp /home/entrenador/kanto/tunel_roca/medium /home/entrenador/kanto/tunel_roca/medalla')
os.system('chmod 000 /home/entrenador/kanto/tunel_roca/medalla')
os.system('chown entrenador:entrenador /home/entrenador/kanto/tunel_roca/medalla')

#Archivo en el que deberan mostrar el contenido de los archivos que esten
#contenidos en el

os.system('rm -rf /home/entrenador/Castillo_de_KingBoo/smash')
os.system('touch /home/entrenador/Castillo_de_KingBoo/smash')

for w in words_from_masks:
	os.system('echo '+ w + ' >> /home/entrenador/Castillo_de_KingBoo/smash')
os.system('echo great_star >> /home/entrenador/Castillo_de_KingBoo/smash')
for i in range(800):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> /home/entrenador/Castillo_de_KingBoo/smash')
os.system('touch /home/entrenador/Castillo_de_KingBoo/great_star')
os.system('echo "superstar" >> /home/entrenador/Castillo_de_KingBoo/great_star')

#_Pipe pregunta (12)

os.system('rm -rf /home/entrenador/Castillo_de_KingBoo/_Pipe')
os.system('mkdir -p /home/entrenador/Castillo_de_KingBoo/_Pipe')
babymario='toad'
babymario_l = map(''.join, itertools.product(*zip(babymario.upper(), babymario.lower())))
dir_babymario = ['_THE','_LEGEND','_OF','_SUPER','_MAC','_BROS']

for z in babymario_l:  #Se mina todo el directorio _TINGLES (nivel 1)
	os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/'+z)
for z in dir_babymario:
	os.system('mkdir -p /home/entrenador/Castillo_de_KingBoo/_Pipe/'+z)
	for a in babymario_l:  #Se minan todos los directorios del segundo nivel
		os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/'+z+'/'+a)
	for x in dir_babymario:
		os.system('mkdir -p /home/entrenador/Castillo_de_KingBoo/_Pipe/'+z+'/'+x)
		for y in dir_babymario:
			os.system('mkdir -p /home/entrenador/Castillo_de_KingBoo/_Pipe/'+z+'/'+x+'/'+y)
			for a in babymario_l:  #Se minan todos los directorios del cuarto nivel
				os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/'+z+'/'+x+'/'+y+'/'+a)

os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/_THE/_LEGEND/Toad')
os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/_OF/_THE/tOAd')
os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/_SUPER/_MAC/toaD')
os.system('touch /home/entrenador/Castillo_de_KingBoo/_Pipe/_BROS/_BROS/ToaD')

#carpetas que comienzen con - para la pregunta (11)

os.system('mkdir -p  /home/entrenador/Castillo_de_KingBoo/_GHOST')
os.system('touch /home/entrenador/Castillo_de_KingBoo/_GHOST/-luigi')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-luigi')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-eas')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-is')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-the')
os.system('mkdir -p /home/entrenador/Castillo_de_KingBoo/-HERO')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-HERO/-of')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-HERO/-this')
os.system('touch /home/entrenador/Castillo_de_KingBoo/-HERO/-world')

DirBasura('/home/entrenador/Castillo_de_KingBoo' , 800)
print " --SE CARGO EL CASTILLO DE KINGBOO"

######################## Fin del CASTILLO DE KINGBOO ########################################################################

#################################
# CASTILLO NUMERO 3 (BOWSER JR.)#
#################################

# Pregunta N 14
# Garantizo que este la carpeta y le agrego lo que necesito
os.system('mkdir /home/entrenador/Castillo_de_Bowser_jr/_under')
os.system('touch /home/entrenador/Castillo_de_Bowser_jr/_under/yoshi')

# Pregunta N 17
# Genera un archivo cOsA con permisos 700 y luego una carpera _kart con permisos 777
os.system('touch /home/entrenador/Castillo_de_Bowser_jr/cOsA && chmod 700 /home/entrenador/Castillo_de_Bowser_jr/cOsA')
os.system('mkdir /home/entrenador/Castillo_de_Bowser_jr/_kart')

aux = respaldo_wfms
aux1 = respaldo_wfms
aux2 = respaldo_wfms

for i in range(50):
    os.system('touch /home/entrenador/Castillo_de_Bowser_jr/_kart/' + aux.pop())


for i in range (10):
    os.system('touch /home/entrenador/Castillo_de_Bowser_jr/_under/' + aux1.pop()[:4])
    os.system('touch /home/entrenador/Castillo_de_Bowser_jr/_under/' + aux2.pop()[:6])

print "---SE CARGO EL CASTILLO DE (BOWSER JR.)"
DirBasura('/home/entrenador/Castillo_de_Bowser_jr' , 800)

######################## Fin del CASTILLO DE BOWSER JR. ########################################################################


#################################
# CASTILLO NUMERO 4 (PIRANA_PLANT)#
#################################

os.system('rm -rf /home/entrenador/Castillo_de_Pirana_plant/_Galaxy')
os.system('rm -rf /home/entrenador/Castillo_de_Pirana_plant/_World')
lineas = respaldo
os.system('mkdir /home/entrenador/Castillo_de_Pirana_plant/_Galaxy')
os.system('mkdir /home/entrenador/Castillo_de_Pirana_plant/_World')
for i in range(800):
	os.system('touch /home/entrenador/Castillo_de_Pirana_plant/_Galaxy/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))
for i in range(600):
	os.system('touch /home/entrenador/Castillo_de_Pirana_plant/_World/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))

os.system('cp -r /home/entrenador/Castillo_de_Pirana_plant/_Galaxy/ /home/entrenador/Castillo_de_Pirana_plant/_Galaxy2')
os.system('cp -r /home/entrenador/Castillo_de_Pirana_plant/_World/ /home/entrenador/Castillo_de_Pirana_plant/_World2')


#archivo random que tendra 30 lineas
os.system('rm -rf /home/entrenador/Castillo_de_Pirana_plant/bigmario')
os.system('touch /home/entrenador/Castillo_de_Pirana_plant/bigmario')
for i in range(30):
    os.system("echo Super EAS Odyssey >> /home/entrenador/Castillo_de_Pirana_plant/bigmario")

#Colocandole 30K a un archivo
os.system('mkdir -p /home/entrenador/Castillo_de_Pirana_plant/BOSS/BOWSER/IS/IN/HIS/')
os.system('touch /home/entrenador/Castillo_de_Pirana_plant/BOSS/BOWSER/IS/IN/HIS/riegame')
for i in range(9999):
    os.system("echo aa >> /home/entrenador/Castillo_de_Pirana_plant/BOSS/BOWSER/IS/IN/HIS/riegame")
os.system('echo "CREETE QUE ERES SUPER EAS... DI EN VOZ ALTA: SOY EAS" >> /home/entrenador/Castillo_de_Pirana_plant/BOSS/BOWSER/IS/IN/HIS/riegame')


os.system('rm -rf /home/entrenador/Castillo_de_Pirana_plant/drmario')
os.system('rm -rf /home/entrenador/Castillo_de_Pirana_plant/mariotetris')

os.system('touch /home/entrenador/Castillo_de_Pirana_plant/drmario')
os.system('touch /home/entrenador/Castillo_de_Pirana_plant/mariotetris')

words_from_masks = respaldo_wfms
for w in words_from_masks:
    	os.system('echo '+ w + '>> /home/entrenador/Castillo_de_Pirana_plant/drmario')

palabra_distinta= 'b0ws3r'
aux = words_from_masks + [palabra_distinta]

shuffle(aux)
for w in aux:
    	os.system('echo '+ w + '>> /home/entrenador/Castillo_de_Pirana_plant/mariotetris')

print '---SE CARGO EL CASTILLO DE (PIRANA_PLANT)'
DirBasura('/home/entrenador/Castillo_de_Pirana_plant/' , 800)

######################## Fin del CASTILLO DE PIRANA_PLANT ###################################################################
