#!/bin/bash

echo " _____________________"
echo "< Let's start scanning! >"
echo " ---------------------"
echo " /\\_/\\  "
echo "( o.o ) "
echo " > ^ <"

IP="$1"
FILE="$2"
FILE2="/home/pduck/nmapscan"
FILE_PORT="${FILE2}/ports/${FILE}"
FILE_DETAIL="${FILE2}/detail/${FILE}"
FILE_VULN="${FILE2}/vuln/${FILE}"
FILE_UDP="${FILE2}/udp/${FILE}"
DIR="/home/pduck/Redteam/${FILE}/dir"


mkdir -pv "$DIR" &>/dev/null
nmap -sS -p- --min-rate 5000 -Pn "$IP" -oA "$FILE_PORT" &>/dev/null
PORT=$(grep open /home/pduck/nmapscan/ports/"$FILE".nmap | awk -F "/" '{print $1}' | paste -sd ",")
echo "port is successful: ${PORT}"

nmap -sT -sC -sV -O -p"$PORT" "$IP" -oA "$FILE_DETAIL" &>/dev/null && echo "detail is successful!" &
nmap --script=vuln -p"$PORT" "$IP" -oA "$FILE_VULN" &>/dev/null && echo "vuln is successful!" &
nmap -sU --top-ports 20 "$IP" -oA "$FILE_UDP" &>/dev/null && echo "udp is successful!" &


# echo "$IP.$FILE,$FILE2,$FILE_PORT,$FILE_DETAIL,$FILE_VULN,$FILE_UDP,$DIR"
gobuster dir -u http://"${IP}" -x rar,zip,php,sql,txt --wordlist=/usr/share/dirbuster/wordlists/directory-list-1.0.txt -o "${DIR}/dir2" --no-error &>/dev/null &
echo "dir is scan yes!"

wait
echo "everything is ok!!"
