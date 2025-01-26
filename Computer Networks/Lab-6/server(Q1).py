import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen(5)

print("Server Activated !")

while True:
    client_socket, address = server_socket.accept()
    print(f"Server connected to client successfully.")
   
    client_message = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {client_message}")

    client_id = client_message.split()[-1]
    
    server_message = f"Hello, I am the server. Your received id is {client_id}"
    
    client_socket.send(server_message.encode('utf-8'))

    client_socket.close()