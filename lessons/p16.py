# PRODUCT CODES 

text = input("Enter the code of the product: ")
def cleaner(text): # takes one argument 
    uppercase = ""
    positives = ""
    negatives = ""
    total_sum = 0
    for item in text:
        if item.isalpha() and item.isupper():
            uppercase += item
            if len(positives) > 0:
                total_sum += int(positives)
                positives = ""
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
        elif item == "-":
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = "-"
            else: 
                negatives = "-"
        elif item.isdigit():
            if len(negatives) > 0: 
                negatives += item 
            else: 
                positives += item
    # end of for loop
    
    #if text ended with a digt
    if len(positives) > 0:
        total_sum += int(positives)
    
    if len(negatives) > 0: 
        total_sum += int(negatives)

    product_code = uppercase + str(total_sum)
    return product_code

result = cleaner(text)
print(result)





#unclean= input("Enter the code of the product: ")
#lowercase = ""
#uppercase = ""
#non_letters = ""
#sum_numbers = int()
#for item in unclean: 
    #if item.isalpha() and item.islower():
        #lowercase += item
    #elif item.isalpha() and item.isupper(): 
        #uppercase += item
   # else: 
        #non_letters += item
    #for non_letters in non_letters:
        #if non_letters in range(1,9):
            #sum_numbers += non_letters
#print(uppercase, sum_numbers)

