import os
import sys
import platform
import datetime
import socket
print("Инфо о пк")
os_name = platform.system()

os_vesion = platform.version()

os_arch = platform.architecture()[0]

Pc_name = platform.node()

API_vers= sys.api_version

print("OC:",os_name, "Версия:", os_vesion, "Количество бит:",os_arch,"Название пк:", Pc_name, "Версия API:", API_vers)


print("Инфо о инете")
hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

print("Хост:", hostname,  "IP:", local_ip)



