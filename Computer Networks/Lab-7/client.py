import socket
import re

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9999))

while True:
    client_name = input("Enter client name: ")
    client_CNIC = input("Enter client CNIC: ")

    pattern_CNIC = r'\d{5}-\d{7}-\d'
    pattern_name = r'^[A-Za-z]+(?: [A-Za-z]+)*$'
    if re.match(pattern_CNIC, client_CNIC) and re.match(
            pattern_name, client_name):
        client_message = client_name + " " + client_CNIC
        client_socket.send(client_message.encode('utf-8'))

        server_response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {server_response}")

        if server_response == 'GET THE POLL':
            poll = input("Enter the poll symbol: ")
            regex1 = r'^[^\d]*$'
            if re.match(regex1, poll):
                client_socket.send(poll.encode('utf-8'))
            else:
                print("Invalid Input")
                continue

        else:
            client_socket.close()
            break

        server_response = client_socket.recv(1024).decode('utf-8')
        print("Server Response: ", server_response)

        client_socket.close()
        break
    else:
        print("Invalid Name or CNIC")
