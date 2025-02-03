def factorial(num):
    # Finding the factorial for a given number using recursve function
    if num == 1: return 1
    else: return num * factorial(num - 1)

def strong_numbers(num):
    temp, sum = num, 0
    
    while temp > 0:
        # Separate the last digit
        # Find factorial for it
        # Add it to the total sum
        sum += factorial(temp % 10)
        temp = temp // 10
    
    return num == sum

if __name__ == "__main__":
    test_cases = [134, 154, 145, 213]
    
    for num in test_cases:
        if strong_numbers(num): print(f"{num} is a Strong Number.")
        else: print(f"{num} is not a Strong Number.")
