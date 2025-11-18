# First algorithm learned: linear search 
#let x represent a string, T be a target character to search 
#let I represent index of a string 
#while i < len(x), if x[i] == T then return i else i + 1
#if T is not found, return - 1

def str_lin_search(text, target): # multi variable function 
    if not text: # len(text) == 0
        return - 1 #any variable that's empty returns true
    else: 
        i = 0
        while i < len(text):
            if text[i] == target: 
                return i 
            i += 1
        # end of while 
        return -1 #delares something was not found

print("Jasper...where is p?", str_lin_search("Jasper", "p")) #linear search is a searching algorithm 