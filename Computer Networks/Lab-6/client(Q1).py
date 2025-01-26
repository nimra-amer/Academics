import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9999))

while True:
    client_id = input("Enter client ID (0-9): ")
    
    if client_id.isdigit() and 0 <= int(client_id) <= 9:

        client_message = f"Hello I am client and My id is {client_id}"
        client_socket.send(client_message.encode('utf-8'))
        
        server_response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {server_response}")

 
        client_socket.close()
        break
    else:
        print("Error: The input should be a digit between 0 and 9.")