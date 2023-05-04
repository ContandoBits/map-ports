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

# Creamos un diccionario para almacenar los puertos abiertos asociados a cada dirección IP
puertos_por_ip = {}

# Recorremos todos los elementos "host" y obtenemos las direcciones IP
for host in root.iter('host'):
    ip = host.find('address').get('addr')
    
    # Recorremos todos los elementos "port" y obtenemos los números de puerto
    puertos_abiertos = []
    for port in host.iter('port'):
        if port.find('state').get('state') == 'open':
            puertos_abiertos.append(port.get('portid'))
    
    # Si se encontraron puertos abiertos para esta dirección IP, los agregamos al diccionario
    if puertos_abiertos:
        puertos_por_ip[ip] = puertos_abiertos

# Generamos el comando nmap para cada dirección IP y sus puertos asociados
for ip, puertos_abiertos in puertos_por_ip.items():
    puertos_cadena = ','.join(puertos_abiertos)
    print("nmap -Pn -n -sV -p " + puertos_cadena + " " + ip)
