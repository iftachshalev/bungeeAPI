import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    s.send(b"ack")

    if data == b"Q":
        print("The Game Break")
        break

    elif data == b"I":
        inp_1 = s.recv(1024).decode()
        inp = input(inp_1)
        s.sendall(inp.encode())

    else:
        print(data.decode())

s.close()
