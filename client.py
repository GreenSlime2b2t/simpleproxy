import requests
import os 
import socket
server_ip = "::1"
server_port = 433
client_address = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
try:
    client_address.connect((server_ip, server_port))
    print("Successfully connected to the server")
    response = client_address.recv(4096)
    print(response.decode("utf-8", errors="ignore"))
finally:
    client_address.close()