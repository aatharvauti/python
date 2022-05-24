import socket

HOST = '192.168.73.250'
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    file = 'img_cat.jpeg'
    with open(file, 'rb') as f:
        img_data = f.read()
        f.close()
    
    s.sendall(img_data)

    # s.sendall(b'Hello, World!')
    data = s.recv(1024)

print(f'Recieved Data: {data!r}')
