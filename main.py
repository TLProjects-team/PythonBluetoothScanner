import bluetooth #pip install pybluez
import os
os.system('mode 60,20')
print('---------------[ BLUETOOTH DEVICES SCANNER ]---------------')
while True:
    devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in devices:
        print('[+] NEW DEVICE:')
        print(f'name: {name}')
        print(f'addr: {addr}')
    print('------------------------[ NEW SCAN ]------------------------')