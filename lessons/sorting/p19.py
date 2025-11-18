# Bubble sort 

def bubble(a_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range (1, len(a_list)):
            if a_list[i -1] > a_list[i]:
                swapped = True
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
        # end of inner for 
    # end of outer while
    return a_list

