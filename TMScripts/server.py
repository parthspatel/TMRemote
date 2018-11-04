import socket

HOST = '127.0.0.1'  # Standard loopback interface, localhost
PORT = 65432        # Listen to port 8673, any port > 1023 are non-privileged ports


# Create a socekt object with IPv4 (AF_INET) & TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # associate the socket with a specific network interface and port number
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()  # server will suspend in this call
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
