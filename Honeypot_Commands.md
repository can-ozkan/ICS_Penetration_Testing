## A simple honeypot
sudo python3 -m honeypots --setup telnet,http,smb,vnc,snmp

## PLC Simulation 1
Change the first half part of the MAC address to 001C06 \
conpot -f --template default \
sudo nmap <IP_address> -Pn -sU -p 16100 \
sudo nmap <IP_address> -Pn -p- \
snmp-check --port 16100 <IP_Address>


## S7 PLC Simulation 2
sudo python3 \
import snap7 \
s7 = snap7.server.Server() \
s7.create() \
s7.start() \
s7.get_status()

python2 plcscan.py 192.168.168.11 \
sudo nmap 192.168.168.11 -Pn -p 102 --script ~/ICS_attack_scripts/Redpoint/s7-enumerate

## Gas Station Controller Simulation
Automatic Tank Gauge
Change the first half part of the MAC address to 00A0F6 \
conpot -f --template guardian_ast \
sudo nmap 192.168.168.12 -Pn -p 10001 --script ~/ICS_attack_scripts/Redpoint/atg-info.nse \
filetype:pdf I20100 \
https://www.veeder.com/us/sites/veeder.com.us/files/2020-09/576013-818%20-%20TLS-3XX%C2%A0Series%20Consoles%20Troubleshooting%20Guide.pdf \
https://www.ericzhang.me/gas-station-atgs-exposed-to-public/ \
telnet 192.168.168.12 10001 \
CTRL + A and I20100 \
Some function codes: \
I20100 1 In-Tank Inventory Report \
I20200 1 In-Tank Delivery Report \
I20300 1 In-Tank Leak Detect Report \
I20400 1 In-Tank Shift Inventory Report \
I20500 1 In-Tank Status Report
  
