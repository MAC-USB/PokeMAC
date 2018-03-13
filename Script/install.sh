#!/bin/bash
USERNAME='entrenador'
PASSWORD='PokeMAC'

if [ $(id -u) -ne 0 ]; then
  echo "Must be root to run this script"
  exit 1
fi

if  [$(id -u $USERNAME) > /dev/null ]; then
  echo "User $USERNAME already exists."
  exit 1
else
  # Create the new user
  useradd "$USERNAME"
  # Add password to the new user
  chpasswd "$USERNAME:$PASSWORD"
fi
