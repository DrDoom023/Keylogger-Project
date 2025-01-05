import socket
import os

PORT = 8080

file_path = 'PATH TO .TXT FILE'  


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(5)

print("Listener started. Waiting for connections...")

while True:
    conn, addr = s.accept()
    with open(file_path, 'a') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data.decode())
