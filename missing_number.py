# You are given an array of n numbers from 1 to n+1, but one number is missing. 
# Find the missing number in O(n) time without using extra space.

def find_missing_number(array):

    # Calculating the sum of series by using traditional formula for the total sum
    original_sum = ((len(array) + 1) * (len(array) + 2)) // 2

    # calculating the actual sum of the elements of the array
    actual_sum = (sum(array))

    # The missing value is the difference between the total sum and the actual sum
    return original_sum - actual_sum

if __name__ == "__main__":
    testcases = [
        [1, 2, 4, 5],         
        [1, 2, 3, 4, 6, 7, 8], 
        [2, 3, 4, 5, 6], 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12],
        [1, 3, 4, 5, 6, 7, 8, 9, 10], 
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    
    for case in testcases:
        print(find_missing_number(case))
