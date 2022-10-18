English="abcdefghijklmnopqrstuvwxyz"

def LEncodeRotn (text="",n=0):
    enc=text.lower()
    dec=""
    for x in range(len(enc)):
        y=(Latin.find(enc[x]))
        dec=dec+(Latin[(y+n) % 26])
    return dec

def LDecodeRotn(text="",n=0):
    dec=text.lower()
    enc=""
    for x in range(len(dec)):
        y=(Latin.find(dec[x]))
        enc=enc+(Latin[((y-n) % 26)])
    return enc    



#Encryption in Latin
t1=input ("Please enter the text to encrypt?")
n1=int(input("please enter rot-n:"))
print("E",n1,"(",t1,")=","(",LEncodeRotn(t1,n1),")",sep="")
print()

#Decryption in Latin
t1=input ("Please enter the text to decrypt?")
n1=int(input("please enter rot-n:"))
print("D",n1,"(",t1,")=","(",LDecodeRotn(t1,n1),")",sep="")
print()
