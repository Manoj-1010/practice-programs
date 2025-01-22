def factorial(n):
    if n < 0: return -1 # Return -1 for negative numbers, since factorial is undefined
    fact, i = 1, 1

    while i <= n:
        fact *= i # Multiplying the existing value and assigning the product to itself
        i += 1
    
    return fact

if __name__ == "__main__":
    print(factorial(5)) # Output: 120
    print(factorial(10)) # Output: 3628800
    print(factorial(-5)) # Output: -1