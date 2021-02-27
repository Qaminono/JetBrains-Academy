import sys
import socket


address = (sys.argv[1], int(sys.argv[2]))

with socket.socket() as client:
    client.connect(address)
    client.send(sys.argv[3].encode())
    response = client.recv(1024)
    response = response.decode()
    print(response)
