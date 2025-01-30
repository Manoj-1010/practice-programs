def perfect_number_check(num):
    # Returning False because numbers less than 2 cannot be a perfect number
    if num < 2: return False

    # Aliquot sum is the sum of all of the factors of a number 
    # except the number itself

    # Since 1 is always present in every aliquot sum 
    # we exclude 1 and add it here
    aliquot_sum = 1 

    for n in range(2,(num//2)+1):
        # If the current number is a factor, we add it to the Aliquot sum
        if num % n == 0: aliquot_sum += n
    
    # A perfect number should the equal to the sum of its factors, except itself
    if num == aliquot_sum: return True
    else: return False


if __name__ == "__main__":
    test_cases = [6, 12, 496, 8128, 2, 28, 100]
    for num in test_cases:
        if perfect_number_check(num): print(f"{num} is a perfect number!")
        else: print(f"{num} is not a perfect number!")
