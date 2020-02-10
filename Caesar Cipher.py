##Created 09/10/2020

##Caesar Cipher Program

##Caesar Cypher for single character
##def Encryption():
##    KeyShift = 4
##    Character = input("Please input a character: ")
##    print(Character)
##    DecValue = ord(Character)
##    print("Decimal value of user input: ",DecValue)
##    NewDecValue = DecValue + KeyShift
##    print("Decimal value after key shift: ",NewDecValue)
##    CharValue = chr(NewDecValue)
##    print("New encrypted character: ",CharValue)

import time

## Casaer Cypher for string Attempt #2
## The program then runs this function in order to encrypt the full string
def encrypt2(string, shift):

  ## Variable 'cipher' is set to blank
  cipher = ''
  ## Selects one character from the string provided
  for char in string:
      ## If the character is a space then it selects the next character
    if char == ' ':
      cipher = cipher + char
    ## If the selected character is upper case then the program converts the
    ## character to its decimal form and then applies the shift. 65 is then
    ## subtracted as uppercase 'A' and lowercase 'a' have different decimal
    ## values. 65 is then added back to the decimal value and the calculation
    ## is complete
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    ## If the selected character is lower case then the program converts the
    ## character to its decimal form and then applies the shift. 97 is then
    ## subtracted as uppercase 'A' and lowercase 'a' have different decimal
    ## values. 97 is then added back to the decimal value and the calculation
    ## is complete
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher

##This code is run first asking for user input string and also a user provided key shift
text = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt2(text, s))
print("")

time.sleep(3)

print("You can now decrypt the message by inputting the encrypted message & key"
      "shift into the below field!")
print("")

time.sleep(3)

## Casaer Cypher Decryption for string Attempt #1
## The program then runs this function in order to encrypt the full string
def Decrypt(string, shift):

  ## Variable 'cipher' is set to blank
  cipher = ''
  ## Selects one character from the string provided
  for char in string:
      ## If the character is a space then it selects the next character
    if char == ' ':
      cipher = cipher + char
    ## If the selected character is upper case then the program converts the
    ## character to its decimal form and then applies the shift. 65 is then
    ## subtracted as uppercase 'A' and lowercase 'a' have different decimal
    ## values. 65 is then added back to the decimal value and the calculation
    ## is complete
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    ## If the selected character is lower case then the program converts the
    ## character to its decimal form and then applies the shift. 97 is then
    ## subtracted as uppercase 'A' and lowercase 'a' have different decimal
    ## values. 97 is then added back to the decimal value and the calculation
    ## is complete
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher

##This code is run first asking for user input string and also a user provided key shift
text = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", text)
print("after decryption: ", Decrypt(text, s))

