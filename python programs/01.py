vow="aeiouAEIOU"
def is_vowel(char):
   if len(char)==1 and char.isalpha():
       return char in vow
   else:
       return false

   char=input("enter a character:")

   if is_vowel(char):
       print(f"{char}is a vowel")
   else:
       print(f"{char}is not a vowel")
