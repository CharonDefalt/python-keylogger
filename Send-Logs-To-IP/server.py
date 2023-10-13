import socket

# Define the server IP and port to listen on
server_ip = '0.0.0.0'  # Listen on all available network interfaces
server_port = 1111

# Create a socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, server_port))
    s.listen()

    print(f"Listening for log messages on {server_ip}:{server_port}...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received log message: {data}")
            # Process the log message as needed
