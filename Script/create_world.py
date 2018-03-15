import os

# CONSTANTS
USERNAME = 'entrenador'
HELPER = 'meowth'
PASSWORD = 'PokeMAC'

# Create the Users and add their passwords
os.system('useradd ' + USERNAME)
os.system('chpasswd ' + USERNAME + ':' + PASSWORD)

os.system('useradd ' + HELPER)
os.system('chpasswd ' + HELPER + ':' + PASSWORD)

# DIRECTORIES (ZONES)
os.system('cp $(pwd)/* /home/meowth')
os.system('mkdir /home/entrenador/kanto/pueblo_paleta')           # Zone 0
os.system('mkdir /home/entrenador/kanto/bosque_verde')            # Zone 1
os.system('mkdir /home/meowth/.poke_oculto/kanto/tunel_roca')     # Zone 2
os.system('mkdir /home/meowth/.poke_oculto/johto/islas_remolino') # Zone 3
os.system('mkdir /home/meowth/.poke_oculto/johto/monte_plateado') # Zone 4

# ALIASES
os.system("echo \"cd /home/entrenador/kanto/\" >> /home/entrenador/.bashrc")
os.system("echo \"alias destello='/home/meowth/scripts/pikachu.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias surf='source /home/meowth/scripts/blastoise.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias vuelo='source /home/meowth/scripts/charizard.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias pokeflauta='/home/meowth/scripts/snorlax.sh'\" >> /home/entrenador/.bashrc")
os.system("echo \"alias instakillred='python /home/invitado/admision/credits.py'\" >> /home/entrenador/.bashrc")
os.system('echo "" > /etc/motd')
os.system('echo "" > /var/run/motd.dynamic')
