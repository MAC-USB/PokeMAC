import os
import crypt

# CONSTANTS
#USERNAME = 'entrenador'
#HELPER = 'meowth'
#PASSWORD = 'PokeMAC'

meowth_passwd = crypt.crypt('ayudame','22')
entrenador_passwd = crypt.crypt('MIQUIMI','22')

os.system('useradd -s /bin/bash -p '+ meowth_passwd +' -m meowth')
os.system('useradd -s /bin/bash -p '+ entrenador_passwd +' -m entrenador')

# Create the Users and add their passwords
# os.system('useradd entrenador')
# os.system('chpasswd entrenador:PokeMAC')

# os.system('useradd meowth')
# os.system('chpasswd meowth:PokeMAC')

# DIRECTORIES (ZONES)
os.system('cp -r $(pwd)/* /home/meowth')
os.system('mkdir -p /home/entrenador/kanto/pueblo_paleta')           # Zone 0
os.system('mkdir -p /home/entrenador/kanto/bosque_verde')            # Zone 1
os.system('mkdir -p /home/meowth/.poke_oculto/kanto/tunel_roca')     # Zone 2
os.system('mkdir -p /home/meowth/.poke_oculto/johto/islas_remolino') # Zone 3
os.system('mkdir -p /home/meowth/.poke_oculto/johto/monte_plateado') # Zone 4

# ALIASES
os.system("echo \"cd /home/entrenador/kanto/\" >> /home/entrenador/.bashrc")
os.system("echo \"alias destello='/home/meowth/scripts/pikachu.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"bash\" >> /home/meowth/.bashrc")
os.system("echo \"bash\" >> /home/entrenador/.bashrc")
os.system("echo \"alias surf='source /home/meowth/scripts/blastoise.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias vuelo='source /home/meowth/scripts/charizard.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias pokeflauta='/home/meowth/scripts/snorlax.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias instakillred='python /home/invitado/admision/credits.py'\" >> /home/entrenador/.bashrc")
# alias instakill="pkill -u meowth -f meowth -KILL; python /home/invitado/admision.credits.py"
os.system('echo "" > /etc/motd')
os.system('echo "" > /var/run/motd.dynamic')
