import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

data = b""

while True:
    inp = input("enter txt:")
    s.sendall(inp.encode())
    while True:
        daata = s.recv(1024)
        if daata[-2] == b"Q":
            break
        else:
            data += daata
            print(daata)
    if data == b"quit":
        print("quit")
        break
    # date = s.recv(1024)
    print('Received:', data)

s.close()
