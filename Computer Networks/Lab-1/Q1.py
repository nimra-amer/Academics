#Q1(part-a)

with open('Input File.txt' , 'r') as file:
  data = file.read()
  print(data)
  
#Q1(part-b)
#integers in file

with open('output1.txt' , 'w+') as file:
  for character in data:
    for letter in character:
        if ord(letter)>=48 and ord(letter)<=57:
            file.write(letter)
            print(letter)

 
#Q1(part-c)
#vowels in file

with open('vowels.txt' , 'w+') as file:
  for character in data:
     for letter in character:
      if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
         file.write(letter)
     
#Q1(part-d)
#non-alphabet

with open('non2.txt' , 'w+') as file:
   for character in data:
     if character >= '65' and character <='90' or character >='97' and character <= '122':
       print(" ")
     else:
       file.write(character)

#Q1(part-e)
with open('Input File.txt' , 'r') as file:
  data1 = file.read()
     
with open('inverted.txt' , 'w+') as file:
  file.write(data1[::-1])
       
