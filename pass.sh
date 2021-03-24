#!bin/bash
red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
cyan='\033[1;36m'
white='\033[1;37m'

clear
echo -e $white"[•]-------------------------------------------[•]"
echo -e $white" |"$cyan"      Author   : Emwe56                      "$white"|"
echo -e $white" |"$red "     Instagram: nano._.emwe                 "$white"|"
echo -e $white" |"$blue"      Tools    : Account Password            "$white"|"
echo -e $white"[•]-------------------------------------------[•]"
echo -e $yellow
 qu="Hai Selamat Datang"
        echo -e $cyan
        read -p "Masukan Nama Anda  : " nama;
        echo -e $purple
        read -p "Masukan Passwordnya: " pass;
        sleep 1
echo -e $blue
echo  $qu $nama
        sleep 1
if [ $pass = "emwe" ]
        then
        echo
        echo -e $green"Password Benar!!"
         sleep 1
         python sms.py
        else
         echo
         echo -e $red"Password Salah!!"
        bash pass.sh
         sleep 1
fi
