#!/usr/bin/python

import itertools
import os
import sys
from random import choice, randint, shuffle
from string import lowercase

f = open('/etc/dictionaries-common/words', 'r')
crap = f.readlines()
backup = crap
f.close()
shuffle(crap)

# FUNCTIONS

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
os.system('touch /home/entrenador/kanto/pueblo_paleta/.ditto')
with open('/home/entrenador/kanto/pueblo_paleta/.ditto', 'a') as f:
    f.write('Lo que buscas comienza con 159.90') # TODO

# 2
create_file('/home/entrenador/kanto/pueblo_paleta/grimer', 100)
with open('/home/entrenador/kanto/pueblo_paleta/grimer', 'a') as f:
    f.write('9.209') # TODO

# 3
create_file('/home/entrenador/kanto/pueblo_paleta/caterpie', 3000) # TODO

print('pueblo_paleta created')

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
os.system('touch /home/entrenador/kanto/bosque_verde/_ATK/##PONME_TODO')
os.system('touch /home/entrenador/kanto/bosque_verde/_DEF/##PONME_TODO')
os.system('touch /home/entrenador/kanto/bosque_verde/_ATK/_LVL/##ESO_PA_LANTE')
os.system('touch /home/entrenador/kanto/bosque_verde/_DEF/_HP/##ESO_PA_LANTE')

# CHALLENGE 5
os.system('find /home/entrenador/kanto/bosque_verde -name POKE | xargs rm -rf')
os.system('touch /home/entrenador/kanto/bosque_verde/POKE')
lineas = backup

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
os.system('echo ":1322eccb acabas_de_conseguir_la_clave" >> /home/entrenador/kanto/bosque_verde/POKE')
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

# CHALLENGE 6
DirBasura("/home/entrenador/kanto/bosque_verde" , 800)

# CHALLENGE 7
masks=['oak','centro','bill','mimo','lago','pokiman','nintendo', 'ho-oh',\
           'geodude','rattata', 'pidgey', 'caterpie']

words_from_masks = []
for i in range(1,300):
    for m in masks:
        num = i % 5
        if num != 0:
            words_from_masks.append(m + str(random_N_digitos(int(num))))

words_from_masks = list(set(words_from_masks))
backup_wfms = words_from_masks

print('bosque_verde created')

#####################
# ZONE 2 - tunel_roca
#####################

# CHALLENGE 8
os.system('rm -rf /home/meowth/.poke_oculto/kanto/tunel_roca/medium')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/medium')

with open('/home/meowth/.poke_oculto/kanto/tunel_roca/medium', 'a') as f:
    # First half of the lines
    for i in range(99):
        random_string = "".join(choice(lowercase) for j in range(6))
        f.write(random_string)
    # Middle line
    f.write('equilibrio')
    # Second half of the lines
    for i in range(100):
        random_string = "".join(choice(lowercase) for j in range(6))
        f.write(random_string)

# CHALLENGE 9
os.system('rm -rf /home/meowth/.poke_oculto/kanto/tunel_roca/medalla')
os.system('cp /home/meowth/.poke_oculto/kanto/tunel_roca/medium /home/meowth/.poke_oculto/kanto/tunel_roca/medalla')
os.system('chmod 000 /home/meowth/.poke_oculto/kanto/tunel_roca/medalla')
os.system('chown entrenador:entrenador /home/meowth/.poke_oculto/kanto/tunel_roca/medalla')

# CHALLENGE 11
os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca/_MGKRP')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_MGKRP/-gary')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-gary')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-EAS')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-is')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-the')
os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca/-HERO')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-HERO/-of')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-HERO/-this')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/-HERO/-world')

# CHALLENGE 12
os.system('rm -rf /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada')
os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada')

KEY_WORD='zubat'
conjugates = map(''.join, itertools.product(*zip(KEY_WORD.upper(), KEY_WORD.lower())))
special_dirs = ['_THE', '_LEGEND', '_OF', '_SUPER','_MAC','_BROS']

# Fill level 1 (_Cascada) with KEY_WORD
for word in conjugates:
    os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/' + word)

for d2 in special_dirs:
    # Generate level 2 directories
    os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/' + d2)

    # Fill level 2 with KEY_WORD
    for w2 in conjugates:
        os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/' + d2 + '/' + w2)

    for d3 in special_dirs:
        # Generate level 3 directories
        os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/' + d2 + '/' + d3)

        # If you payed attention, you will realise that level 3 is the only one
        # isn't filled with random files. We will add the key files later. This
        # is what we want the prenewbies to find.

        for d4 in special_dirs:
            # Generate level 4 directories
            os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/' + d2 + '/' + d3 + '/' + d4)

            # Fill level 4 with KEY_WORD
            for w4 in conjugates:
                os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/' + d2 + '/' + d3 + '/' + d4 + '/' + w4)

# These are the level 3 files that we want the prenewbies to find
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/_THE/_LEGEND/zubat')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/_OF/_THE/ZuBaT')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/_SUPER/_MAC/zUbAt')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/_Cascada/_BROS/_BROS/ZUBAT')

# CHALLENGE 13
os.system('rm -rf /home/meowth/.poke_oculto/kanto/tunel_roca/golpe')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/golpe')

for w in words_from_masks:
	os.system('echo '+ w + ' >> /home/meowth/.poke_oculto/kanto/tunel_roca/golpe')
os.system('echo master_ball >> /home/meowth/.poke_oculto/kanto/tunel_roca/golpe')
for i in range(800):
	os.system('echo "'+(((lineas.pop()).lower()).replace("'",":")).strip("\n")+'" >> /home/meowth/.poke_oculto/kanto/tunel_roca/golpe')
os.system('touch /home/meowth/.poke_oculto/kanto/tunel_roca/master_ball')
os.system('echo "hidro" >> /home/meowth/.poke_oculto/kanto/tunel_roca/master_ball')

DirBasura('/home/meowth/.poke_oculto/kanto/tunel_roca' , 800)

print('tunel_roca created')

#########################
# ZONE 3 - islas_remolino
#########################

# CHALLENGE 14
os.system('mkdir /home/meowth/.poke_oculto/johto/islas_remolino/_under')
os.system('touch /home/meowth/.poke_oculto/johto/islas_remolino/_under/lugia')

aux1 = backup_wfms
aux2 = backup_wfms

for i in range (10):
    os.system('touch /home/meowth/.poke_oculto/johto/islas_remolino/_under/' + aux1.pop()[:4])
    os.system('touch /home/meowth/.poke_oculto/johto/islas_remolino/_under/' + aux2.pop()[:6])

# CHALLENGE 17
os.system('touch /home/meowth/.poke_oculto/johto/islas_remolino/tORRe && chmod 603 /home/meowth/.poke_oculto/johto/islas_remolino/tORRe')
os.system('mkdir /home/meowth/.poke_oculto/johto/islas_remolino/_campana')

aux = backup_wfms

for i in range(50):
    os.system('touch /home/meowth/.poke_oculto/johto/islas_remolino/_campana/' + aux.pop())

DirBasura('/home/meowth/.poke_oculto/johto/islas_remolino' , 800)

print('islas_remolino created')

#########################
# ZONE 4 - monte_plateado
#########################

# CHALLENGE 18
os.system('rm -rf /home/meowth/.poke_oculto/johto/monte_plateado/_Grass')
os.system('rm -rf /home/meowth/.poke_oculto/johto/monte_plateado/_Region')
lineas = backup
os.system('mkdir /home/meowth/.poke_oculto/johto/monte_plateado/_Grass')
os.system('mkdir /home/meowth/.poke_oculto/johto/monte_plateado/_Region')
for i in range(800):
	os.system('touch /home/meowth/.poke_oculto/johto/monte_plateado/_Grass/' + (((lineas.pop()).lower()).replace("'",":")).strip("\n"))
for i in range(600):
	os.system('touch /home/meowth/.poke_oculto/johto/monte_plateado/_Region/' + (((lineas.pop()).lower()).replace("'",":")).strip("\n"))

os.system('cp -r /home/meowth/.poke_oculto/johto/monte_plateado/_Grass/ /home/meowth/.poke_oculto/johto/monte_plateado/_Grass2')
os.system('cp -r /home/meowth/.poke_oculto/johto/monte_plateado/_Region/ /home/meowth/.poke_oculto/johto/monte_plateado/_Region2')

# CHALLENGE 21
os.system('rm -rf /home/meowth/.poke_oculto/johto/monte_plateado/gyarados')
os.system('touch /home/meowth/.poke_oculto/johto/monte_plateado/gyarados')
for i in range(30):
    os.system("echo Super EAS Odyssey >> /home/meowth/.poke_oculto/johto/monte_plateado/gyarados")

#Colocandole 30K a un archivo
os.system('mkdir -p /home/meowth/.poke_oculto/johto/monte_plateado/JEFE/RED/EN/SU/')
os.system('touch /home/meowth/.poke_oculto/johto/monte_plateado/JEFE/RED/EN/SU/JUEGO')
for i in range(9999):
    os.system("echo aa >> /home/meowth/.poke_oculto/johto/monte_plateado/JEFE/RED/EN/SU/JUEGO")
os.system('echo "CREETE QUE ERES SUPER EAS... DI EN VOZ ALTA: SOY EAS" >> /home/meowth/.poke_oculto/johto/monte_plateado/JEFE/RED/EN/SU/JUEGO')

# CHALLENGE 22
os.system('rm -rf /home/meowth/.poke_oculto/johto/monte_plateado/eevee-saur')
os.system('rm -rf /home/meowth/.poke_oculto/johto/monte_plateado/ivy-saur')

os.system('touch /home/meowth/.poke_oculto/johto/monte_plateado/eevee-saur')
os.system('touch /home/meowth/.poke_oculto/johto/monte_plateado/ivy-saur')

words_from_masks = backup_wfms
for w in words_from_masks:
    os.system('echo '+ w + '>> /home/meowth/.poke_oculto/johto/monte_plateado/eevee-saur')

palabra_distinta= 'r3D'
aux = words_from_masks + [palabra_distinta]

shuffle(aux)
for w in aux:
    os.system('echo '+ w + '>> /home/meowth/.poke_oculto/johto/monte_plateado/ivy-saur')

print('monte_plateado created')

DirBasura('/home/meowth/.poke_oculto/johto/monte_plateado/', 800)
