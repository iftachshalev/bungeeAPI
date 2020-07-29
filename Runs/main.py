from Game.Maneger import Manager
import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()
conn, addr = s.accept()

conn.sendall(b"I")
ROBOT_ARRAY = []
ack = conn.recv(1024)
if ack != b"ack":
    raise ConnectionError("ack is'nt receive")

conn.sendall(b"Shoos number of players:\n >>>")
ROBOT_NUM_USER = conn.recv(1024)
ROBOT_NUM_USER = int(ROBOT_NUM_USER)
for i in range(ROBOT_NUM_USER):
    e = str(i + 1)
    ctr = "player " + e + ":"
    conn.sendall(ctr.encode())
    ack = conn.recv(1024)
    if ack != b"ack":
        raise ConnectionError("ack is'nt receive")
    conn.sendall(b"I")
    ack = conn.recv(1024)
    if ack != b"ack":
        raise ConnectionError("ack is'nt receive")
    conn.sendall(b" Robot [R] or player [P]?")
    rp = conn.recv(1024)
    if rp == b"R":
        conn.sendall(b"I")
        ack = conn.recv(1024)
        if ack != b"ack":
            raise ConnectionError("ack is'nt receive")
        conn.sendall(b" What is the level? [1, 2, 3]:")
        lv = conn.recv(1024)
        ROBOT_ARRAY.append(int(lv.decode()))
    elif rp == b"P":
        ROBOT_ARRAY.append(0)
    conn.sendall(b" The player saved!")
    ack = conn.recv(1024)
    if ack != b"ack":
        raise ConnectionError("ack is'nt receive")


# while True:
#     ROBOT_NUM_USER = input("Shoos number of players:\n >>>")
#     try:
#         ROBOT_NUM_USER = int(ROBOT_NUM_USER)
#
#         break
#     except:
#         print("Error!!!")
#
# ROBOT_ARRAY = []
# for i in range(ROBOT_NUM_USER):
#     succses = False
#     while succses is False:
#         print("player", i + 1, ":")
#         input_1 = input(" Robot [R] or player [P]?")
#         if input_1 == "P":
#             ROBOT_ARRAY.append(0)
#             succses = True
#             print(" The player saved!")
#         elif input_1 == "R":
#             while True:
#                 input_2 = input(" What is the level? [1, 2, 3]:")
#                 try:
#                     input_2 = int(input_2)
#                     if input_2 > 3 or input_2 < 1:
#                         print(" Error!!!")
#                     else:
#                         break
#                 except:
#                     print(" Error!!!")
#             ROBOT_ARRAY.append(input_2)
#             print(" The player saved!")
#             succses = True
d = Manager(conn, ROBOT_ARRAY)
t = d.run()

