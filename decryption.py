a=input("Write the encrypted form:-")
key=int(input("Give the key: "))
print("The decrypted form is:-",end='')    
for i in range(len(a)):
    c=[ord(a[i])]
    for j in range(len(c)):
       d=(c[j]-key)%256
       print(chr(d),end='')
       