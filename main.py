import os
Loop="True"
while Loop:
    print('''
._____________________________________________________.          
|Welcome to Encoder/Decoder Program written in Pyhton.|
|This program  encodes/decodes  given  text in various|
|methods. It will encode/decode in Latin or in Turkish|
|succesively. The methods included are:               |
|                                                     | 
|1. Rotn Cipher                                       |
|2. Vigenere Cipher                                   |
|3. Prime Number Indexing Cipher                      |
·_____________________________________________________·          
| Please choose your method:                          |                         
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
    elif x==3:
        print('''
    ********************************
    * Prime Number Encoder/Decoder *
    ********************************
      ''')  
        os.system("python3 primenumber.py")
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
