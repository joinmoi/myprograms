#String checklist 

# 1. create an empty string 
empty_string = ""
ver2 = ''

# 2. determine if a string is empty 
if not str_var: 
    print("str_var is empty!") # -> method one 

if len(str_var) == 0:
    print ("str_var is empty!") # -> method two

# 3. format a string to contain dynamic data 
name = "fluffington"
str_var = f"Hello{name}!" # allows to inject dynamic data into a string

# 4. access individual characters/items in a string 
name = "fluffington"
print(name[0]) # you would get f 
print(name[-2]) # you would get o

# 5. access the first, access the last item in a string
name = "fluffington"
print(name[0]) #zero index is always the first 
print(name[len(name)-1]) # this gives last 
print(name[-1]) # also gives last

# 6. join two/multiple strings together 
a = "poo"
b = "poo"
c = a + b
print(c) # we expect poopoo

# 7. reverse a string 
temp = "park"
reversed_temp = temp[:: -1]
v2 = "".join(reversed(temp))

# 8. create a copy of a string
temp = "hydroflask"
temp_copy = temp[:]
another_copy = temp

# 9. compare strings quality
a = "marshall"
b = "dog"
status = a == b

# 10. determine the minimum and maximum value within a string
temp = "hydroflask"
print(max(temp)) # it will grab whichever is positioned the latest --> y
print(min(temp)) # it will grab whichever is positioned first --> a
print(max("hello", "goodbye")) # grabs the "bigger" string
print(min('1', '2', '3', '!'))

# 11. determine if an item or a pattern exists within a string
word = "poopooplatter"
if "poo" in word:
    print("there is poo!")

# 12. locate the index of an item or a pattern whithin a string
word = "poopooplatter"
poop_location = word.fiind("poo") # won't crash if it can't find
poop_location = word.index("poop") # code won't work

# 13. count how often an item or a pattern occurs within a string
word = "poopooplatter"
poop_count = word.count("poo")

# 14. convert all items ina string to uppercase/lowercase
yell_hydroflask = "hydroflask".upper()
calm_hydroflask = yell_hydroflask.lower()

# 15. determine if the string can be converted to an integer 
str_num = "67"
num = 0
if str_num.isdigit():
    num = int(str_num) # 16. convert a string to an integer 

# 17. determine if a string only contains alphabetical characgters
word = "shsm".isalpha()

# 18. remove non-alphabetical characters from a string 
# sometimes it's easier to create than remove 
gibberish = "34t8w39shgsghsiughs!eiseuhsiueghsi3453453"
clean = "" 
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1

# 19. remove all alphabetical characters from a string 
gibberish = "34t8w39shgsghsiughs!eiseuhsiueghsi3453453"
clean = "" 
i = 0
while i < len(gibberish):
    # if not gibberish[i].isalpha() == False:
    if not gibberish[i].isalpha(): 
        clean += gibberish[i]
    i += 1

# 20. remove all whitespaces from a string 
example = "h h h h h h h e l         l o "
example - example.replace(" ", "") #target the whitespace and change it to an empty

# 21. sort a string in ASCII order or reverse-ASCII order 

# 22. determine if a string follows a ruleset

