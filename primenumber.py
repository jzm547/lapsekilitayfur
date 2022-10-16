Turkish="abcçdefgğhıijklmnoöprsştuüvyz"
Latin="abcdefghijklmnopqrstuvwxyz"

def indextoprime(n=0):
    prime_numbers = [2,3]
    i=3
    if(0<n<3):
        return prime_numbers[n-1]
    elif(n>2):
        while (True):
            i+=1
            status = True
            for j in range(2,int(i/2)+1):
                if(i%j==0):
                    status = False
                    break
            if(status==True):
                prime_numbers.append(i)
            if(len(prime_numbers)==n):
                break
        return prime_numbers[n-1]

def LEncodePrime (text="",key=""):
    text=text.lower()
    key=key.lower()
    enc=""
    keyindex = [0] * int(len(key))
    for x in range(len(key)):
        keyindex[x]=(Latin.find(key[x]))
    i=-1
    n=0
    for x in range(len(text)):
        y=(Latin.find(text[x]))
        i=i+1
        if i==len(key):
            i=0 
        n=int(keyindex[i])
        enc=enc+(Latin[((y+n) % 26)])
    return enc

def LDecodePrime (text="",key=""):
    text=text.lower()
    key=key.lower()
    enc=""
    keyindex = [0] * int(len(key))
    for x in range(len(key)):
        keyindex[x]=(Latin.find(key[x]))
    i=-1
    n=0
    for x in range(len(text)):
        y=(Latin.find(text[x]))
        i=i+1
        if i==len(key):
            i=0 
        n=int(keyindex[i])
        enc=enc+(Latin[((y-n) % 26)])
    return enc

def TEncodePrime (text="",key=""):
    text=text.lower()
    key=key.lower()
    enc=""
    keyindex = [0] * int(len(key))
    for x in range(len(key)):
        keyindex[x]=(Turkish.find(key[x]))
    i=-1
    n=0
    for x in range(len(text)):
        y=(Turkish.find(text[x]))
        i=i+1
        if i==len(key):
            i=0 
        n=int(keyindex[i])
        enc=enc+(Turkish[((y+n) % 29)])
    return enc

def TDecodePrime (text="",key=""):
    text=text.lower()
    key=key.lower()
    enc=""
    keyindex = [0] * int(len(key))
    for x in range(len(key)):
        keyindex[x]=(Turkish.find(key[x]))
    i=-1
    n=0
    for x in range(len(text)):
        y=(Turkish.find(text[x]))
        i=i+1
        if i==len(key):
            i=0 
        n=int(keyindex[i])
        enc=enc+(Turkish[((y-n) % 29)])
    return enc
        
#Prime Number Encryption in Latin
t1=input ("Please enter the text the encrypt with Prime Numbers:")
fprime=int(input ("Please enter first prime index:"))
lprime=int(input ("Please enter last prime index:"))
t2=""
for x in range (fprime,lprime):
    t2=t2+Latin[indextoprime(x) % 26]   
print("E{P",fprime,"-",lprime,"}(",t1,")=(",LEncodePrime(t1,t2),")",sep="")
print()          
          
#Prime Number Decryption in Latin
t1=input ("Please enter the text the decrypt with Prime Numbers:")
fprime=int(input ("Please enter first prime index:"))
lprime=int(input ("Please enter last prime index:"))
t2=""
for x in range (fprime,lprime):
    t2=t2+Latin[indextoprime(x) % 26]  
print("E{P",fprime,"-",lprime,"}(",t1,")=(",LDecodePrime(t1,t2),")",sep="")
print()

#Prime Number Encryption in Turkish
t1=input ("Asal sayılarla şifrelenecek metin:")
fprime=int(input ("İlk asal sayının indeksi:"))
lprime=int(input ("Son asal sayının indeksi:"))
t2=""
for x in range (fprime,lprime):
    t2=t2+Latin[indextoprime(x) % 29]   
print("E{P",fprime,"-",lprime,"}(",t1,")=(",TEncodePrime(t1,t2),")",sep="")
print()          
          
#Prime Number Decryption in Turkish
t1=input ("Please enter the text the decrypt with Prime Numbers:")
fprime=int(input ("İlk asal sayının indexi:"))
lprime=int(input ("Son asal sayının indeksi:"))
t2=""
for x in range (fprime,lprime):
    t2=t2+Latin[indextoprime(x) % 29]  
print("E{P",fprime,"-",lprime,"}(",t1,")=(",TDecodePrime(t1,t2),")",sep="")
print()

