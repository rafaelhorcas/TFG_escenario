@echo off
netsh interface ipv4 add address "Ethernet 2" 10.0.3.2 255.255.255.0 gateway="10.0.3.1"
route -p add 10.0.1.0 MASK 255.255.255.0 10.0.3.1
netsh interface ipv4 add address "Ethernet 3" 10.0.0.16 255.255.255.0 
route -p add 10.0.0.0 MASK 255.255.255.0 10.0.0.13
echo Configuracion de red completada
