## Prerequisite Downloads and Commands
sudo apt-get install python3-pip \
sudo pip3 install honeypots \
pip install pysmi \
pip install pysnmp \
pip install pyasn1 \
pip3 install conpot \
export PATH="$PATH:/home/can/.local/bin" \
source ~/.bashrc \
sudo pip3 install python-snap7 \
sudo ufw disable

If you have IEC problem, downgrade the scapy version and other libraries: \
pip install scapy==2.4.5 \
pip install pysmi==0.3.4 \
pip install pysnmp==4.4.12 \
pip install pyasn1==0.4.8

## Attack Scripts for Kali Linux
https://github.com/meeas/plcscan \
https://github.com/tijldeneut/ICSSecurityScripts \
https://sourceforge.net/projects/modbuspal/files/modbuspal/RC%20version%201.6b/ \
https://github.com/digitalbond/Redpoint \
sudo gem install modbus-cli \
modbus --help \
https://github.com/sourceperl/mbtget 

## Common Pentest Tools
netdiscover \
nmap \
snmp-check \
metasploit (msfconsole) \
searchsploit
