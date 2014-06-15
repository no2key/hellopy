import socket

HOST = '127.0.0.1'
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    message = input('客户端：')
    s.sendall(message.encode())
    data = s.recv(4096)
    print('服务器：{}'.format(data.decode()))
s.close()



