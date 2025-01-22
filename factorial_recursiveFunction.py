def factorial(n):
    '''
        Factorial using recursive function
            1. Return -1 for negative numbers
            2. Return 1 for zero
            3. Recursively call the function with the previous number of the given to multiply the result to generate factorial
    '''
    if n < 0: return -1 
    if n == 0: return 1 
    return  n * factorial(n-1)  

if __name__ == "__main__":
    print(factorial(6)) # Output: 720
    print(factorial(-5)) # Output: -1