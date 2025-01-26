import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen(5)

print("Server Activated!")

with open('Voters_List.txt', 'r') as file:
    voters = [line.strip() for line in file.readlines()]

symbols = {}
with open('Candidates_List.txt', 'r') as file1:
    for line in file1.readlines():
        line = line.strip()
        if line:
            candidate, symbol = line.split(':')
            symbols[candidate.strip()] = symbol.strip()

already_voted = set()


def handle_client(client_socket):
    client_message = client_socket.recv(1024).decode('utf-8')
    print("Received from client: ", client_message)

    data = client_message.split(" ")
    name = " ".join(data[:-1])
    CNIC = data[-1]

    vote = f"{name}/{CNIC}"

    if vote in voters and CNIC not in already_voted:
        print("Candidates and Symbols:")
        for candidate, symbol in symbols.items():
            print(candidate, " ", symbol)

        server_message = "GET THE POLL"
        client_socket.send(server_message.encode('utf-8'))

        already_voted.add(CNIC)

        poll_symbol = client_socket.recv(1024).decode('utf-8').strip()

        valid_symbol = False
        for candidate, symbol in symbols.items():
            if poll_symbol.lower() == symbol.lower():
                valid_symbol = True
                print(
                    f"You have casted your vote for {candidate} with symbol {symbol} successfully"
                )

                with open('output_file.txt', 'a') as file1:
                    file1.write(
                        f"Candidate: {candidate},\tSymbol: {symbol},\tCNIC: {CNIC}\n"
                    )
                break

        if valid_symbol:
            server_message = "Vote Casted Successfully"
        else:
            server_message = "Invalid symbol. Vote not cast."
    else:
        server_message = "Name or CNIC of voter is not available, or you have already voted."

    client_socket.send(server_message.encode('utf-8'))
    client_socket.close()


while True:
    client_socket, address = server_socket.accept()
    print("Server connected to client successfully.")

    client_thread = threading.Thread(target=handle_client,
                                     args=(client_socket, ))
    client_thread.start()
