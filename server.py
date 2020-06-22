import socket
from Game.Messages import StartGameMessage


HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()
conn, addr = s.accept()

print('Connected by', addr)

while True:
    data = conn.recv(1024)
    print(data)
    if data == b"Q":
        conn.sendall(b"quit")
        break
    a = StartGameMessage(1, 2, [2, 3, 5, 10, 0], 9)
    conn.sendall(a.encode())
    #conn.sendall(str(len(data)).encode() + str(data)[-2].encode())

conn.close()
s.close()
