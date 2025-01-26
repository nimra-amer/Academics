import socket
import threading

max_clients = 3

sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets.bind(('0.0.0.0', 12345))
sockets.listen(max_clients)
print("Server Activated!!")

while True:
  client_socket, client_address = sockets.accept()

  if threading.active_count() - 1 < max_clients:
    print("Connection Made")

    def client_thread():
      while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'DISCONNECT':
          print("Client", client_address, "has disconnected.")
          break
        print("Received from", client_address, ":", message)
        client_socket.send(message.encode('utf-8'))

      client_socket.close()

    threading.Thread(target=client_thread).start()

  else:
    client_socket.send(b"Server Full")
    client_socket.close()
