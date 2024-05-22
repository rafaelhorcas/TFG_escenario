@echo off
netsh interface ipv4 add address "Ethernet 2" 10.0.1.2 255.255.255.0 gateway="10.0.1.1"
route -p add 10.0.3.0 MASK 255.255.255.0 10.0.1.1
echo Configuracion de red completada
