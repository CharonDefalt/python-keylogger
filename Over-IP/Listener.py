import socket

def receive_logs(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print(f"Listening for logs on {ip}:{port}...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    while True:
        received_data = client_socket.recv(1024).decode()
        if received_data:
            print(f"Received data: {received_data}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    IP_ADDRESS = "192.168.121.105"   ################## Change it to your ip
    PORT = 85                        ################## Change it to your custom port OR dont change it on Both scripts
    receive_logs(IP_ADDRESS, PORT)
