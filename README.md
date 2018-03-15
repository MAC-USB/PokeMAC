# PokeMAC

PokeMAC is a project for Tarea 3 Admisión Enero Marzo 2018.

The project will be divided in two sections: Script and WebApp.

1. **Script:** This will generate the users and configurations in Sala A pc's.
2. **WebApp:** Will generate the UI to authenticate some data and help the
   prenewbies to understand some concepts and guide them.


Here will be more information soon to provide a guide to future MAckenzies.

## Install Instructions

### Client side

Clone the repo and change into the directory
```sh
$ git clone https://github.com/MAC-USB/PokeMAC.git
$ cd PokeMAC/Script
```

Run the scripts:
```sh
$ sudo python create_world.py
$ python fill_world.py
```

* `create_world.py` generates the base structure of the game. It requires
  `sudo` because it creates two users (**entrenador** and **meowth**).
* `fill_world.py` populates the base structure with A LOT of random and useless
  stuff, but also adds the necessary files for the challenges.

Once the script populates the world, you can start playing loging as the user
**meowth** in the **tty1** and as **entrenador** in the **tty2**

```sh
$
```
