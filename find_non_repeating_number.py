def find_single_number(array):
    result = 0
    for num in array:
        # Performing XOR operation with 0 gives back the same number
        # If same numbers undergo XOR operation, they become 0
        # Only the unique number stands at last at result variable
        result = num ^ result
    
    return result

if __name__ == "__main__":
    test_cases = [
    [2, 2, 1],
    [4, 1, 2, 1, 2],
    [1],
    [7, 3, 5, 3, 7],
    [9, 9, 8, 8, 7, 7, 6],
    [10, 11, 12, 11, 10],
    [100, 200, 300, 200, 100],
    [5, 6, 5, 6, 7, 7, 8],
    [42],
    [0, 1, 0] ]

    for array in test_cases:
        print(find_single_number(array))
