import pycipher
key = input("key:\n")
password = input("password:\n")
str1 = pycipher.Vigenere(key).decipher(password) # encipher 加密
print(str1)