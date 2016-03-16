import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_addr = ('0.0.0.0', 2222)

sock.bind(sock_addr)
sock.listen(10)

while True:
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if 'close' not in data:
            conn.sendall(data)
        else:
            conn.close()
            break
