def biggest_digit(num):
    # Assume 0 as the biggest digit value
    result = 0
    
    while num > 0:
        # Get each digit from reverse
        # And store it in a variable
        rem = num % 10
        
        # If the value of result is lesser
        # Than that of rem
        # Replace the value of result by rem
        if rem > result:
            result = rem
        
        num = num // 10
        
    # Return the final result
    return result

if __name__ == "__main__":
    test_cases = [32, 97, 3287, 1273, 18726]
    
    for num in test_cases:
        print(f"{biggest_digit(num)} is the biggest digit of {num}")
