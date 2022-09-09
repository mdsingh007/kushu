import ipaddress
import socket
def host_name(ip_address):
    a = socket.gethostbyaddr(ip_address)
    return a[0]

print(host_name("185.228.168.9"))