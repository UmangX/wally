#!/bin/bash

# ref: https://askubuntu.com/a/30157/8698
if ! [ $(id -u) = 0 ]; then
   echo "The script need to be run as root." >&2
   exit 1
fi

if [ $SUDO_USER ]; then
    real_user=$SUDO_USER
else
    real_user=$(whoami)
fi

if ! command -v feh &> /dev/null
then
    echo "feh is not installed use apt or pacman to install feh"
    exit
fi
cp wally.py wally 
pip3 install -r requirements.txt
sudo chmod +x wally 
sudo mv wally /usr/bin/
