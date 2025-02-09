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
