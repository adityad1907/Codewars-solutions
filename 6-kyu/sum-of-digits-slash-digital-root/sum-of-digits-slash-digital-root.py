def digital_root(n):
    while len(str(n))>1:
        total = 0
        for digits in str(n):
            total += int(digits)
            n = total
    return n # your code here