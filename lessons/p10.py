#string stuff
# tacocat is a palindrome 
# like dogged, 906609
def is_palindrome(word):
    #checks is argument word is a plaindrome 
    return word == word[::-1]

text = input("enter a word: ")
if is_plaindrome(text):
    print(f"{text} is a plindrome.")
else: 
    print(f"{text} is boring")