def smallest_number(num1, num2):
    # Compare if first number is greater than second.
    # If true, return True, or else return False
    if num1 > num2: return True
    else: return False

if __name__ == "__main__":
    test_cases = [[2,5], [7, 4], [10, 13], [93, 98], [21, 19]]

    # Test the function for various testcases
    for pair in test_cases:
        if smallest_number(pair[0], pair[1]):
            print(f"{pair[0]} is greater than {pair[1]}")
        else:
            print(f"{pair[1]} is greater than {pair[0]}")
