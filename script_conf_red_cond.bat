@echo off
netsh interface ipv4 add address "rem-switch" 10.0.3.2 255.255.255.0 gateway="10.0.3.1"
netsh interface ipv4 add address "qos-switch" 10.0.0.16 255.255.255.0 gateway="10.0.2.12"
echo Configuracion de red completada
