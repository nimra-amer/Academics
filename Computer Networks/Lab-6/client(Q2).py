import socket 

def reverse_non_vowel_words(sentence): 
    vowels = "aeiouAEIOU" 
    words = sentence.split() 
    result = [] 
    for word in words: 
        if not any(vowel in word for vowel in vowels): 
            result.append(word[::-1]) 
        else: 
            result.append(word)
    return ' '.join(result) 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(('127.0.0.1', 9999)) 
client_message = input("Enter a string: ")

client_socket.send(client_message.encode('utf-8')) 
server_response = client_socket.recv(1024).decode('utf-8')  

client_result = reverse_non_vowel_words(server_response) 
print("Client Result : " , client_result) 
client_socket.close()
