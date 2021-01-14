#Förskjutningschiffer, uppgift från Åbo Akademi sommaren 2020. Kod skriven av René Selander.

'''
import string... (ASCII-kod), behövs inte här och nu.

Källa: https://www.w3schools.com/python/ref_string_isalpha.asp The isalpha() method returns True if all the characters are alphabet letters (a-z).
'''

#Anger hur många bokstäver som ska användas:
alfa_26 = 26 

#Funktionen kryptera eller dekryptera:
def crypt_or_decrypt():

  while True:

      print(f'Hej, vill du kryptera (k) eller dekryptera (d) ett meddelande?')

      mode = input().lower()

      if mode in 'kryptera k dekryptera d'.split():

         return mode

      else:

         print(f'Välj bokstaven k om du vill kryptera eller bokstaven d om du vill dekryptera.')

#Funktionen som tar emot användarens input:
def get_message():

     print(f'Skriv ditt meddelande eller ord: ')

     return input()

#Funktion som tar emot användarens val av nyckel:
def get_key():

     key = 0

     while True:

         print(f'Ange nyckeln (ett nummer mellan 1 och 26): ')

         key = int(input())

         if (key >= 1 and key <= alfa_26):

             return key

#Funktion som behandlar all data och returnerar den till print(final_output):
def final_output(mode, message, key):

     if mode[0] == 'd':

         key = -key

     processed = ''

     for character in message:

         if character.isalpha():

             num = ord(character)

             num += key

             if character.isupper():

                 if num > ord('Z'):

                     num -= 26

                 elif num < ord('A'):

                     num += 26

             elif character.islower():

                 if num > ord('z'):

                     num -= 26

                 elif num < ord('a'):

                     num += 26

             processed += chr(num)

         else:

             processed += character

     return processed

mode = crypt_or_decrypt()

get_message = get_message()

get_key = get_key()

print(f'Ditt krypterade meddelande är: ')

#Följande rad skriver ut det krypterade eller dekrypterade meddelande eller ordet.
print(final_output(mode, get_message, get_key))