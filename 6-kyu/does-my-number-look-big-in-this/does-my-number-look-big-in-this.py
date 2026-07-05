def narcissistic( value ):
    digits = str(value)
    power = len(digits)
    
    total = sum(int(d) ** power for d in digits)
    return total == value # Code away