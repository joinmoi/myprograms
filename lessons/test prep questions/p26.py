# dictionaries 
# For each numbers from 2 to N (N → integer user input)
# Create a key, value pair of its Factors

def factors(x): 
    result = []
    for v in range(1, x+1): 
        if x % v == 0: 
            result.append(x)
        return result
        
num = int(input("Number: "))
   for n in range(2, num+1):
    table[n] = factors(n)

# question 46 hw question 
def collatz_seq(num): 
    size = 1
    start = num 
    while start > 1: 
        if start % 2 == 0: 
            start = start // 2
        else: 
            start *= 3 
            start += 1 
        size += 1 
    return size 
# end up collatz

def f(word):
    if len(word) <= 1: 
        return True 
    elif (len(word)) <= 3: 
        return word[0] == word[-1]
    else: 
        return word[0] == word[-1] and f(word[1:-1])
