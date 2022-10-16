Turkish="abcçdefgğhıijklmnoöprsştuüvyz"
Latin="abcdefghijklmnopqrstuvwxyz"

def LEncodeVigenere (text="",key=""):
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

def LDecodeVigenere (text="",key=""):
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

def TEncodeVigenere (text="",key=""):
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

def TDecodeVigenere (text="",key=""):
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
        
#Vigenere Encryption in Latin
t1=input ("Please enter the text the encypt with Vigenere:")
t2=input ("Please enter secret key:")
print("E(",t1,",",t2,")=(",LEncodeVigenere(t1,t2),")",sep="")
print()          
          
#Vigenere Decryption in Latin
t1=input ("Please enter the text the encypt with Vigenere:")
t2=input ("Please enter secret key:")
print("E(",t1,",",t2,")=(",LDecodeVigenere(t1,t2),")",sep="")
print()  

#Vigenere Encryption in Turkish
t1=input ("Vigenere ile şifrelenecek metin:")
t2=input ("Gizli anahtar:")
print("E(",t1,",",t2,")=(",TEncodeVigenere(t1,t2),")",sep="")
print()          
          
#Vigenere Decryption in Turkish
t1=input ("Vigenere ile şifrelenecek metin:")
t2=input ("Gizli anahtar:")
print("E(",t1,",",t2,")=(",TDecodeVigenere(t1,t2),")",sep="")
