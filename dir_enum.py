import os
import requests
import sys

#Verificaci[n de argumentos
if len(sys.argv) != 3:
    sys.exit(1)

file = sys.argv[1]
path = os.path.join(os.getcwd(), file)

try:
    with open(path, 'r') as f:
        sub_list = f.read()
except FileNotFoundError:
    print(f"El archivo {file} no ha sido encontrado en la ruta.")
    sys.exit(1)

directories = sub_list.splitlines()
valid_count = 0

#Compruebaci[on de directorios
for dir in directories:
    dir_enum = f"http://{sys.argv[2]}/{dir}.html"
    try:
        r = requests.get(dir_enum)
        if r.status_code != 404:
            print("Directorio válido:", dir_enum)
            valid_count += 1
    except requests.ConnectionError:
        print(f"No se pudo conectar a {dir_enum}.")
print(f"Cantidad de directorios válidos encontrados: {valid_count}")
