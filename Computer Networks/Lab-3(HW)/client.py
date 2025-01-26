import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    input_message = input(
        "Enter message or enter 'DISCONNECT' to exit (disconnect) from the server : "
    )
    client_socket.send(input_message.encode('utf-8'))

    if input_message == "DISCONNECT":
        print("Disconnected")
        break

    recv_message = client_socket.recv(1024).decode('utf-8')
    print("Received from server: ", recv_message)

client_socket.close()
