import socket

HOST = '192.168.73.250'
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET: IPv4
    # SOCK_STREAM: TCP 
    s.bind((HOST, PORT))

    s.listen()
    print('Waiting for a connection...')

    conn, addr = s.accept()
    print('New Connection established...')

    with conn:
        print(f'Connected by: {addr}')

        while True:
            data = conn.recv(1024)

            file = 'img_cat.jpeg'
            with open(file, 'ab') as f:
                f.write(data)
                f.close()
            
            if not data or len(data) < 1024:
                break
        conn.sendall(b'Finished Data Transfer!')