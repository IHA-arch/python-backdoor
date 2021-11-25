#!/bin/bash

root() {
user=`whoami`
if [[ $user != 'root' ]]; then
	echo "Please run as root\n"
	exit
fi
}

access() {
cp backdoor /usr/local/bin
chmod +x /usr/local/bin/backdoor

mkdir /usr/share/backdoor_IHA >& /dev/null
cp backdoor-python.sh /usr/share/backdoor_IHA
cp listen.py /usr/share/backdoor_IHA
sleep 1
printf "\ntype 'backdoor' anywhere on the terminal\n"
}

root
access


