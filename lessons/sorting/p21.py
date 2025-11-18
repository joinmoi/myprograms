# sorting challenge 
# order a_list while b_list is getting sorted

def inserty(a_list, b_list):
    i = 1 
    while i < len(a_list):
        j = 1 
        while j > 0: 
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_lsit[j-1]
                b_list[j-1], b_list[j] = b_list[j], 
            else: 
                break
            j -= 1 
        i += 1
