def digital_root(n):
    while len(str(n))>1:
        sum = 0
        for digits in str(n):
            sum += int(digits)
            
            n = sum 
    return n 