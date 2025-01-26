
import socket

def reverse_vowel_words(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    result = []
    for word in words:
        if any(vowel in word for vowel in vowels):
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen(5)

print("Server Activated !!")

while True:
    client_socket, address = server_socket.accept()
    print(f"Serve and Client Connected Successfully")
    
    client_message = client_socket.recv(1024).decode('utf-8')
    print("Received from client: " , client_message)
    
    result = reverse_vowel_words(client_message)
    print("Response : " , result)
    server_response = reverse_vowel_words(client_message)
    client_socket.send(server_response.encode('utf-8'))
    
    client_socket.close()