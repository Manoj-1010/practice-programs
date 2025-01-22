def factorial(n):
    if n < 0: return -1 # Return -1 for negative numbers, since factorial is undefined for negative numbers

    fact = 1
    for i in range(1, n+1):
        fact *= i # Multiplying the existing value and assigning the product to itself
    
    return fact

if __name__ == "__main__":
    print(factorial(5)) # Output: 120
    print(factorial(-3)) # Output: -1