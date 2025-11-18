# non-destructive selection sort with lists 

def select(a_list): 
    if len(a_list) <= 1:
        return a_list
    else: 
        i = 0
        while i < len(a_list):
            smallest = a_list[i] # -> accesses each value in a_list within current_value , prove if it is or it is not
            # lets go hunting 
            j = i + 1 # search from i + 1 onwards 
            new_location = i # initalize to i 
        
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest: 
                    smallest = new_value
                    new_location = j
                j += 1
            # end of hunting

            # swap the smallest into the proper location 
            temporary = a_list[i]
            a_list[i] = smallest
            a_list[new_location] = temporary
            # ^ how you swap two values

            #python way 
            # a_lsit[i], a_list[new_location] = a_lsit[new_location], a_list[i]
            i += 1
