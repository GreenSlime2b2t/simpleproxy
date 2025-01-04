import requests
import os 
import socket

PORT = 433
HOST = "::"
hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname)
print(ipv4)
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
print(server_socket)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("Server is waiting for connections...")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established from {client_address}")
    try:
        url=""
        headers = {
            "User-Agent" : "ProxyServer"
        }
        response = requests.get(url, headers=headers)

        client_socket.send(response.content)
    except Exception as e:
        print(f"Error forwarding {e}")
    client_socket.close()
