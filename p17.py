#create an empty list 
a_list = []
b_list = ()

# determine if a string is empty 
if not a_list: # more efficient 
    print("a_list is empty")
if len(a_list) == 0:
    print("a_list is empty")

# what does len(), sum(), min(), max() do when a list is an argument 
c_list = [3,1,4,1,5,9] 
print(len(c_list)) # expect 6
print(sum(c_list)) # 23
print(min(c_list)) # 1
print(max(c_list)) # 9 - largest value in the list
# min and max do linear search

# access individual items in a list
d_list = list("hello, world!")
# there would be square bracket, all the letters are individual in the list
print(d_list[0]) # "h" -> access first item
print(d_list[-1]) # "!" -> access last item
print(d_list[1:4]) # ["e", "l", "l"]

# join two/multiple lists together 
a = [3, 1, 4]
b = ["Marshall", "Freya", "Joy"]
c = a + b # this creates a new list of a and b joined
a.extend(b) # mutates a to give the contents of b
a = [3, 1, 4]
for item in b:
    a.append(item)

# reverse a list (two ways)
# create a copy of a list (two ways) 
# compare lists for equality 
# determine if an item exists within a list 
# locate the index of an item within a list 
# count how often an item occurs within a list 
# convert a string to a list 
# sort a list 
# sort two lsits where the index are attached to each other based on