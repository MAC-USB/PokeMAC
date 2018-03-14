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
<<<<<<< HEAD:Script/fill_world.py
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >> /home/entrenador/kanto/bosque_verde/POKE')
os.system('echo ":1352eccba Meowth_dice_que_la_clave_es_nxt" >> /home/entrenador/kanto/bosque_verde/POKE')
=======
	os.system('echo ":'+str(random_N_digitos(4))+str0+'" >>  /home/entrenador/kanto/bosque_verde/STAR')
os.system('echo ":1352eccba aMeowthlegustanlasgalletas" >>  /home/entrenador/kanto/bosque_verde/STAR')
>>>>>>> features/dialogues__1:Script/gen_world.py
for i in range(300):
	str0 = "".join(choice(lowercase) for j in range(27))
	os.system('echo ":' + str(random_N_digitos(4)) + str0 + '" >>  /home/entrenador/kanto/bosque_verde/POKE')
for i in range(50):
	os.system('echo "' + (((lineas.pop()).lower()).replace("'",":")).strip("\n") + '" >>  /home/entrenador/kanto/bosque_verde/POKE')

DirBasura("/home/entrenador/kanto/bosque_verde" , 800)

<<<<<<< HEAD:Script/fill_world.py

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
=======
######################## Fin del bosque_verde ########################################################################

###############################
# REGION NUMERO 2 (TUNEL_ROCA)#
###############################
#DE AQUI EN ADELANTE TODAS ESTARAN EN OPT OCULTAS
os.system('rm -rf /home/entrenador/tunel_roca/block')
os.system('touch /home/entrenador/tunel_roca/block')
for i in range(99):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >>  /home/entrenador/tunel_roca/block')
os.system('echo mushroom >>  /home/entrenador/tunel_roca/block')     #Essta es la linea del medio
for i in range(100):
	str0 = "".join(choice(lowercase) for j in range(6))
	os.system('echo '+str0+' >>  /home/entrenador/tunel_roca/block')

os.system('rm -rf Taquirule/templo_E/coin')
os.system('cp /home/entrenador/tunel_roca/block /home/entrenador/tunel_roca/coin')
os.system('chmod 000 /home/entrenador/tunel_roca/coin ; chown entrenador:entrenador /home/entrenador/tunel_roca/coin')


#Cosas de la pregunta 7
masks=['oldpokeball','region','bicicleta','balas','repelente','misty','nintendo', 'sunshine',\
           'brocoli','pokegym','mochila', 'ataque']

words_from_masks = []
for i in range(1,300):
    for m in masks:
        num = i % 5
        if num != 0:
            words_from_masks.append(m + str(random_N_digitos(int(num))))

words_from_masks = list(set(words_from_masks))
respaldo_wfms = words_from_masks
>>>>>>> features/dialogues__1:Script/gen_world.py

#Archivo en el que deberan mostrar el contenido de los archivos que esten
#contenidos en el

os.system('rm -rf /home/entrenador/tunel_roca/smash')
os.system('touch /home/entrenador/tunel_roca/smash')

for w in words_from_masks:
	os.system('echo '+ w + ' >> /home/entrenador/tunel_roca/smash')
os.system('echo great_star >> /home/entrenador/tunel_roca/smash')
for i in range(800):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> /home/entrenador/tunel_roca/smash')
os.system('touch /home/entrenador/tunel_roca/great_star')
os.system('echo "superstar" >> /home/entrenador/tunel_roca/great_star')

#_Pipe pregunta (12)

os.system('rm -rf /home/entrenador/tunel_roca/_Pipe')
os.system('mkdir -p /home/entrenador/tunel_roca/_Pipe')
babymario='toad'
babymario_l = map(''.join, itertools.product(*zip(babymario.upper(), babymario.lower())))
############No se que colocar aqui
dir_babymario = ['_THE','_ADVENTURE','_OF','_SUPER','_POKEMAC','_TRAINERS']

for z in babymario_l:  #Se mina todo el directorio _TINGLES (nivel 1)
	os.system('touch /home/entrenador/tunel_roca/_Pipe/'+z)
for z in dir_babymario:
	os.system('mkdir -p /home/entrenador/tunel_roca/_Pipe/'+z)
	for a in babymario_l:  #Se minan todos los directorios del segundo nivel
		os.system('touch /home/entrenador/tunel_roca/_Pipe/'+z+'/'+a)
	for x in dir_babymario:
		os.system('mkdir -p /home/entrenador/tunel_roca/_Pipe/'+z+'/'+x)
		for y in dir_babymario:
			os.system('mkdir -p /home/entrenador/tunel_roca/_Pipe/'+z+'/'+x+'/'+y)
			for a in babymario_l:  #Se minan todos los directorios del cuarto nivel
				os.system('touch /home/entrenador/tunel_roca/_Pipe/'+z+'/'+x+'/'+y+'/'+a)

os.system('touch /home/entrenador/tunel_roca/_Pipe/_THE/_ADVENTURE/Zubat')
os.system('touch /home/entrenador/tunel_roca/_Pipe/_OF/_THE/zUBat')
os.system('touch /home/entrenador/tunel_roca/_Pipe/_SUPER/_POKEMAC/zubaT')
os.system('touch /home/entrenador/tunel_roca/_Pipe/_TRAINERS/_TRAINERS/zUbAt')

#carpetas que comienzen con - para la pregunta (11)

os.system('mkdir -p  /home/entrenador/tunel_roca/_GHOST')
os.system('touch /home/entrenador/tunel_roca/_GHOST/-ash')
os.system('touch /home/entrenador/tunel_roca/-ash')
os.system('touch /home/entrenador/tunel_roca/-profesorEAS')
os.system('touch /home/entrenador/tunel_roca/-is')
os.system('touch /home/entrenador/tunel_roca/-the')
os.system('mkdir -p /home/entrenador/tunel_roca/-TRAINER')
os.system('touch /home/entrenador/tunel_roca/-TRAINER/-of')
os.system('touch /home/entrenador/tunel_roca/-TRAINER/-this')
os.system('touch /home/entrenador/tunel_roca/-TRAINER/-region')

DirBasura('/home/entrenador/tunel_roca' , 800)
print " --SE CARGO EL TUNEL ROCA"

######################## Fin del TUNEL ROCA ########################################################################

#################################
#REGION NUMERO 3 (ISLAS REMOLINO)#
#################################

# Pregunta N 14
# Garantizo que este la carpeta y le agrego lo que necesito
os.system('mkdir /home/entrenador/islas_remolino/_under')
os.system('touch /home/entrenador/islas_remolino/_under/yoshi')

# Pregunta N 17
# Genera un archivo cOsA con permisos 700 y luego una carpera _kart con permisos 777
os.system('touch /home/entrenador/islas_remolino/cOsA && chmod 700 /home/entrenador/islas_remolino/cOsA')
os.system('mkdir /home/entrenador/islas_remolino/_kart')

aux = respaldo_wfms
aux1 = respaldo_wfms
aux2 = respaldo_wfms

for i in range(50):
    os.system('touch /home/entrenador/islas_remolino/_kart/' + aux.pop())


for i in range (10):
    os.system('touch /home/entrenador/islas_remolino/_under/' + aux1.pop()[:4])
    os.system('touch /home/entrenador/islas_remolino/_under/' + aux2.pop()[:6])

print "---SE CARGO ISLAS REMOLINO"
DirBasura('/home/entrenador/islas_remolino' , 800)

######################## Fin de ISLAS REMOLINO ########################################################################


#################################
#REGION NUMERO 4 (MONTE PLATEADO)#
#################################

os.system('rm -rf /home/entrenador/monte_plateado/_Galaxy')
os.system('rm -rf /home/entrenador/monte_plateado/_World')
lineas = respaldo
os.system('mkdir /home/entrenador/monte_plateado/_Galaxy')
os.system('mkdir /home/entrenador/monte_plateado/_World')
for i in range(800):
	os.system('touch /home/entrenador/monte_plateado/_Galaxy/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))
for i in range(600):
	os.system('touch /home/entrenador/monte_plateado/_World/'+(((lineas.pop()).lower()).replace("'",":")).strip("\n"))

os.system('cp -r /home/entrenador/monte_plateado/_Galaxy/ /home/entrenador/monte_plateado/_Galaxy2')
os.system('cp -r /home/entrenador/monte_plateado/_World/ /home/entrenador/monte_plateado/_World2')


#archivo random que tendra 30 lineas
os.system('rm -rf /home/entrenador/monte_plateado/bigmario')
os.system('touch /home/entrenador/monte_plateado/bigmario')
for i in range(30):
    os.system("echo Super EAS Odyssey >> /home/entrenador/monte_plateado/bigmario")

#Colocandole 30K a un archivo
os.system('mkdir -p /home/entrenador/monte_plateado/BOSS/BOWSER/IS/IN/HIS/')
os.system('touch /home/entrenador/monte_plateado/BOSS/BOWSER/IS/IN/HIS/riegame')
for i in range(9999):
    os.system("echo aa >> /home/entrenador/monte_plateado/BOSS/BOWSER/IS/IN/HIS/riegame")
os.system('echo "CREETE QUE ERES SUPER EAS... DI EN VOZ ALTA: SOY EAS" >> /home/entrenador/monte_plateado/BOSS/BOWSER/IS/IN/HIS/riegame')


os.system('rm -rf /home/entrenador/monte_plateado/drmario')
os.system('rm -rf /home/entrenador/monte_plateado/mariotetris')

os.system('touch /home/entrenador/monte_plateado/drmario')
os.system('touch /home/entrenador/monte_plateado/mariotetris')

words_from_masks = respaldo_wfms
for w in words_from_masks:
    	os.system('echo '+ w + '>> /home/entrenador/monte_plateado/drmario')

palabra_distinta= 'b0ws3r'
aux = words_from_masks + [palabra_distinta]

shuffle(aux)
for w in aux:
    	os.system('echo '+ w + '>> /home/entrenador/monte_plateado/mariotetris')

<<<<<<< HEAD:Script/fill_world.py
print '---SE CARGO EL CASTILLO DE (PIRANA_PLANT)'
DirBasura('/home/entrenador/Castillo_de_Pirana_plant/' , 800)
=======


print '---SE CARGO EL MONTE PLATEADO'
DirBasura('/home/entrenador/monte_plateado' , 800)
>>>>>>> features/dialogues__1:Script/gen_world.py

######################## Fin del CASTILLO DE PIRANA_PLANT ###################################################################
