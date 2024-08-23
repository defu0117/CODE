#!/bin/bash

echo " _____________________"
echo "< Let's start scanning! >"
echo " ---------------------"
echo " /\\_/\\  "
echo "( o.o ) "
echo " > ^ <"

# $1 is IP,$2 is scan os name; eg: ./scripts 192.168.10.6 bados

IP="$1"
FILE="$2"

name=$(whoami)
FILE2="/home/${name}/nmapscan"
FILE_PORT="${FILE2}/ports/${FILE}"
FILE_DETAIL="${FILE2}/detail/${FILE}"
FILE_VULN="${FILE2}/vuln/${FILE}"
FILE_UDP="${FILE2}/udp/${FILE}"
DIR="/home/${name}/Redteam/${FILE}/dir"

if [ -d $DIR ]; then
	echo "dir exists"	
else
	mkdir -pv "$DIR" &>/dev/null
	echo "dir be created"
fi

sudo nmap -sS -p- --min-rate 5000 -Pn "$IP" -oA "$FILE_PORT" &>/dev/null  

PORT=$(grep open /home/${name}/nmapscan/ports/"$FILE".nmap | awk -F "/" '{print $1}' | paste -sd ",")
echo "port is successful: ${PORT}"

sudo nmap -sTCV -O -p"$PORT" "$IP" -oA "$FILE_DETAIL" &>/dev/null && echo "detail is successful!" &
sudo nmap --script=vuln -p"$PORT" "$IP" -oA "$FILE_VULN" &>/dev/null && echo "vuln is successful!" &
sudo nmap -sU --top-ports 20 "$IP" -oA "$FILE_UDP" &>/dev/null && echo "udp is successful!" &


# echo "$IP.$FILE,$FILE2,$FILE_PORT,$FILE_DETAIL,$FILE_VULN,$FILE_UDP,$DIR"
sudo gobuster dir -u http://"${IP}" -x rar,zip,php,sql,txt --wordlist=/usr/share/dirbuster/wordlists/directory-list-1.0.txt -o "${DIR}/dir2" --no-error &>/dev/null &
echo "dir is scan yes!"

wait
echo "everything is ok!!"
