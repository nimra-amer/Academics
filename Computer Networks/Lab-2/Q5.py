import re
i = 0
web = []
with open('file.txt' , 'r') as file:
  for URL in file:
    web.append(URL.strip())
    
print (web)

regex = r'\.[a-zA-Z0-9]{2,}$' #if only extraction
#regex = r'\.[a-zA-Z]{2,}$' #id checking the validation

for url in web:
    result = re.search(regex, url)
    if result:
        print (result.group())
