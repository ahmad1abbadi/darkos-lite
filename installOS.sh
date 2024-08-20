#!/bin/bash
clear
echo "Updating termux packages list please wait"
apt update &>/dev/null
echo "Upgrading termux packages...this might take some time"
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade >/dev/null
while true; do
	termux-setup-storage
	sleep 4
    if [[ -d ~/storage ]]; then
        break
    else
        echo -e "Storage permission denied"
    fi
    sleep 2
done
apt install python --no-install-recommends -y &>/dev/null
echo "be patient"
curl -o installglibc.py https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/installglibc.py && python3 installglibc.py
exit
