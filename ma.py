"""""""""""""""""""""""
import nmap

ip = "192.168.1.60"
print(f"Iniciando escaneo IP: {ip}\n\t Esto puede tardar unos minutos...")
s = nmap.PortScanner()
s.scan(ip)

print("Escaneo finalizado")
print(s[ip])

"""""""""""""""""""""
import nmap

# Dirección IP a escanear
ip = "192.168.1.60"
print(f"Iniciando escaneo IP: {ip}\n\t Esto puede tardar unos minutos...")

# Crear un objeto PortScanner
scanner = nmap.PortScanner()

# Realizar el escaneo
scanner.scan(ip, arguments='-p 1-65535 -T4')

print("Escaneo finalizado")

# Mostrar los puertos abiertos
print(f"\nHost: {ip}")
for proto in scanner[ip].all_protocols():
    print(f"\nProtocolo: {proto}")
    lport = scanner[ip][proto].keys()
    for port in lport:
        print(f"Puerto: {port}\tEstado: {scanner[ip][proto][port]['state']}")




