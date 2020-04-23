import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()
conn, addr = s.accept()

print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if data == b"Q":
        conn.sendall(b"quit")
        break
    conn.sendall(str(len(data)).encode() + str(data)[-2].encode())




conn.close()
s.close()
