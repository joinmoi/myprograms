#anagram function

def anagram(t1, t2):
    if not t1 and not t2:
        return -1 
    elif len(t1) != len(t2):
        print("it's not an anagram")
        
    i1 = 0
    i2 = 0
    while len(t1) == len(t2): 
        t1 = t1.lower()
        t2 = t2.lower()

        if t1[i1].isalpha() == t2[i2].isalpha():
            return t1, t2

word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")
print(anagramt1, t2" they are anagrams of each other")