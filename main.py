import os
Loop="True"
while Loop:
    print('''
        
Welcome to Message Conversion Program written in Pyhton.
This program  enrypts/decrypts  given  text in various
methods.  The methods included are:               
|                                                     
1. Rotn Cipher                                       
2. Vigenere Cipher                                   
                              
 Please choose your method:                                                  
    ''')

    x=int(input())
    if x==1:
      print('''
    *************************
    * Rot-n Encoder/Decoder *
    *************************
            
      ''')
      os.system("python3 rotn.py")
    elif x==2:
        print('''
    ****************************
    * Vigenere Encoder/Decoder *
    ****************************
      ''')
        os.system("python3 vigenere.py")
    else:
        print("please enter 1,2 or 3!")
    
    a=input("Do you want to encode/decode again? (y/n)")
    if a=="n":
      Loop="False"
      print("have a good day!")
      break
    else:
      print()
      print()
      Loop="True"           
