import os
from crypt import crypt

# CONSTANTS
USERNAME = 'entrenador'
HELPER = 'meowth'
PASSWORD = crypt('POKEMAC','22')

os.system('useradd -s /bin/bash -p ' + PASSWORD + ' -m' + HELPER)
os.system('useradd -s /bin/bash -p ' + PASSWORD + ' -m' + USERNAME)

print('Users created')

# DIRECTORIES (ZONES)
os.system('cp -r $(pwd)/* /home/meowth/')
os.system('mkdir -p /home/entrenador/kanto/pueblo_paleta; chmod 755 /home/entrenador/kanto/pueblo_paleta')
os.system('mkdir -p /home/entrenador/kanto/bosque_verde; chmod 700 /home/entrenador/kanto/bosque_verde')
os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca; chmod 700 /home/meowth/.poke_oculto')
os.system('mkdir -p /home/meowth/.poke_oculto/johto/islas_remolino')
os.system('mkdir -p /home/meowth/.poke_oculto/johto/monte_plateado')

print('Base directories created')

# ALIASES
os.system("echo \"cd /home/entrenador/kanto/\" >> /home/entrenador/.bashrc")
os.system("echo \"alias ayudame='fg'\" >> /home/meowth/.bashrc")
os.system("echo \"alias destello='/home/meowth/scripts/pikachu.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias surf='source /home/meowth/scripts/blastoise.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias vuelo='source /home/meowth/scripts/charizard.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias pokeflauta='/home/meowth/scripts/snorlax.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias instakillred='python /home/invitado/admision/credits.py'\" >> /home/entrenador/.bashrc")
# alias instakill="pkill -u meowth -f meowth -KILL; python /home/invitado/admision.credits.py"

os.system("echo \"[[ -r ~/.bashrc  ]] && . ~/.bashrc\" >> /home/entrenador/.bash_profile")
os.system("echo \"[[ -r ~/.bashrc  ]] && . ~/.bashrc\" >> /home/meowth/.bash_profile")

os.system('echo "" > /etc/motd')
os.system('echo "" > /var/run/motd.dynamic')

print('Aliases created')
