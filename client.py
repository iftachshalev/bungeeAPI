import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('54.157.229.65', 65432))
to_res = my_socket.recv(1024)
print(to_res); input_1 = input("your turn:")
my_socket.send(b'input_1')
