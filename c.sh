#!/bin/bash

clear
echo "\033[1;32m        START "
sleep 2s

ulang="y"

while [ $ulang = "y" ]
do

python skelethonwae2.py &
python skelethonvalue.py &
python skelethonwae2.py &
python skelethonwae2.py
x=3
while [ $x -gt 0 ]
do
sleep 1s
clear
echo " \033[1;32m Mulai ulang sisa Waktu anda didunia $x Detik"
x=$(( $x - 1 ))
done

done