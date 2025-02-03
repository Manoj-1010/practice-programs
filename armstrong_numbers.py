import math
def armstrong_numbers(num):
    # Calculaing the number of digits in the given number
    n = math.floor(math.log10(num)+1)
    
    sum = 0
    temp = num
    
    while temp > 0:
        # Raising every digit by the power of number of digits
        sum += (temp % 10) ** n
        temp = temp // 10
    
    return num == sum

if __name__ == "__main__":
    test_cases = [325, 17, 5, 153]
    
    for num in test_cases:
        if armstrong_numbers(num): print(f"{num} is an Armstrong number")
        
        else: print(f"{num} is not an Armstrong number")
