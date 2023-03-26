import sys
import xml.etree.ElementTree as ET

# Verificamos que se haya proporcionado el nombre del archivo XML como argumento
if len(sys.argv) < 2:
    print("Debe proporcionar el nombre del archivo XML generado por Nmap como argumento.")
    sys.exit(1)

# Obtenemos el nombre del archivo XML del primer argumento
archivo_xml = sys.argv[1]

# Cargamos el archivo XML generado por Nmap
tree = ET.parse(archivo_xml)

# Obtenemos la raíz del árbol
root = tree.getroot()

# Obtenemos la dirección IP escaneada
ip = root.find('host/address').get('addr')

# Recorremos todos los elementos "port" y obtenemos los números de puerto
puertos_abiertos = []
for port in root.iter('port'):
    if port.find('state').get('state') == 'open':
        puertos_abiertos.append(port.get('portid'))

# Almacenamos los puertos abiertos separados por comas
puertos_cadena = ','.join(puertos_abiertos)
print("nmap -Pn -n -sV -p " + puertos_cadena + " " +ip)
