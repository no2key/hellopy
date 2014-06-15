import socket

HOST = '127.0.0.1'
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
c, address = s.accept()

print('成功与{}建立连接'.format(address))

while True:
    data = c.recv(4096)
    if not data:
        break
    print('客户端:{}'.format(data.decode()))
    message = input('服务器：')
    c.send(message.encode())
c.close()