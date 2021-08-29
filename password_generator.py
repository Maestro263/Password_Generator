import random

letters = "abcdefghijklmnopqrstuvxyz"
big_letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "1234567890"
symboler = "(){}[],."

mix = letters + big_letters + numbers + symboler
length = 22

kode = "".join(random.sample(mix,length))
print(kode)
