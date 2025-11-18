# test prep question 

def mean(a_list): 
    total = 0
    for i in data: 
        total += i 
        mean = total / len(a_list)
    return mean
result = mean(DATA)
print(f"The mean is {result}")

def meadian(a_list): 
    swapped = True 
    while swapped: 
        swapped = False 
        for i in range (1, len(a_list)): 
            if a_list[i-1] > a_list[i]: 
                swapped == True 
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
    # end of sorting 
def median(a_list): 
    a_list = bubble(a_list)
    if len(a_list) % 2 == 0: 
        middle_index1 = len(a_list) // 2 - 1
        middle_index2 = len(a_list) // 2
        meanie = (a_list[middle_index1] + a_list[middle_index2]) / 2  
        return meanie
    else: 
        middle_index = len(a_list) // 2
        return middle_index 

result = median(DATA)
print(f"Median is {result}")  
