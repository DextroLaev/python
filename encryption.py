word=input("Write the encrypted form:-")
key=int(input("Give the key: "))

print("The decrypted form is:-",end='')    

for asciicode in range(len(word)):

    ascii=[ord(word[asciicode])]

    for asciialpha in range(len(ascii)):

       d=(ascii[asciialpha]+key)%256

       print(chr(d),end='')
    

