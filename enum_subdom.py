import os
import requests
import sys

if len(sys.argv) != 3:
    sys.exit(1)

file = sys.argv[1]
path = os.path.join(os.getcwd(), file)

try:
    with open(path, 'r') as f:
        sub_list = f.read()
except FileNotFoundError:
    print(f"El archivo {file} no se encuentra dentro de esta ruta.")
    sys.exit(1)

subdoms = sub_list.splitlines()

# Comprobaci[on de dominios
for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[2]}"
    try:
        response = requests.get(sub_domains)
        if response.status_code == 200:
            print("Dominio válido:", sub_domains)
    except requests.ConnectionError:
        pass
