#string practice 

#cleaning 
def clean(text):
    # to return a string with everyting lowercased 
    # and without special character nor numbers 
    result = ""
    i = 0 # avoid index b/c it is a function
    while i < len(text):
        if text[i].isalpha(): 
        # .isalpha() returns True if the given character is alphabetical  
            result = result + text[i].lower()
        i += 1
        # end of while loop 
    return result

word = input("Enter a word: ")
print (clean(word))

