def check_prime(n):
    '''
        Check if the given number is Prime or not
            1. Set the flag to True and counter variable to '2' by default
            2. Check for divisibility of the number till it's half using while loop
            3. If divisible, set flag to False
            4. Return Flag
    '''
    flag = True
    i = 2

    while i <= n//2:
        if n % i == 0: flag = False
        i +=1
    
    return flag

if __name__ == "__main__":
    num1, num2 = 5, 6

    if check_prime(num1): print(f"{num1} is a prime.") # Output: 5 is not a prime.
    else: print(f"{num1} is not a prime.")

    if check_prime(num2): print(f"{num2} is a prime.")
    else: print(f"{num2} is not a prime.") #Output: 6 is not a prime.