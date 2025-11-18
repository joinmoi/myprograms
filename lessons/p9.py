#fibonacci number 
def fibonacci(num):
    if num in {0,1}:
        return num
    else:
        count = 2
        a = 0
        b = 1
        while count <= num:
            total = a + b
            a = b
            b = total 
            count += 1 
        return total
 i = 0 
 while i < 10:
    
    
