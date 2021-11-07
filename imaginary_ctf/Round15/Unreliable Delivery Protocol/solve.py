#nc -u to connect to UDP port

import socket


address = ("13.90.75.65",7331)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# SOCK_DGRAM == UDP

sock.sendto(b'test123',address)

print(sock.recv(2048).decode())