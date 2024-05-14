@echo off
netsh interface ipv4 add address "veh-switch" 10.0.2.2 255.255.255.0 gateway="10.0.2.1"
echo Configuracion de red completada
