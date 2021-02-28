import sys
import socket
from itertools import product


def generate_password():
    index = 1
    while True:
        abc = 'abcdefghijklmnopqrstuvwxyz1234567890'
        yield from product(abc, repeat=index)
        index += 1


address = (sys.argv[1], int(sys.argv[2]))


with socket.socket() as client:
    client.connect(address)
    res = ""
    generator = generate_password()
    while res != "Connection success!":
        password = "".join(next(generator))
        client.send(password.encode())
        response = client.recv(1024)
        res = response.decode()
    print(password)
