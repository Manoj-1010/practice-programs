def second_last_digit(num):
    # Remove the last digit from the number
    num = num // 10
    
    # Return the last digit now
    # Which is the second last digit
    return num % 10

if __name__ == "__main__":
    test_cases = [298, 49827, 219837, 12786, 13]
    
    for num in test_cases:
        print(f"{second_last_digit(num)} is the second last digit of {num}")
