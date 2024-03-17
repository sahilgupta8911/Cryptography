import random 
from wonderwords import RandomSentence
import string


original = RandomSentence()
original = original.sentence()
s = original.translate(str.maketrans('', '', string.punctuation)).upper().replace(" ", "")

key_len = random.randint(6,10)
key = [random.randint(1,26) for i in range(key_len)]

message = []
for c in s:
    message.append(ord(c)-64)

encoded = [0 for i in range(len(message))]
k=0

for i in range(len(message)):
    encoded[i] = (message[i]+key[k]-1)%26
    k = (k+1)%key_len
    
print(key_len)

for i in range(len(encoded)):
        encoded[i] = chr(ord('A') + encoded[i])
encoded = " ".join(encoded)
print(encoded)

for i in range(len(message)):
        message[i] = chr(ord('A') + message[i]-1)
message = "".join(message)
# print(message)

for i in range(key_len):
        key[i] = chr(ord('A') + key[i]-1)
key = "".join(key)
# print(key)

while(True):
    n = input("Enter final answer, or else enter 'a' to quit:")
    if(n==message):
        print("You win!")
        print(key)
        print(message)
        print(original)
        break
    elif(n=='a'):
        print('You lose!')
        print(key)
        print(message)
        print(original)
        break
    else:
        print('try again')

    