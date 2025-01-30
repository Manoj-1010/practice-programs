#Given an integer n, return a string array answer (1-indexed) where:
#    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#    answer[i] == "Fizz" if i is divisible by 3.
#    answer[i] == "Buzz" if i is divisible by 5.
#    answer[i] == i (as a string) if none of the above conditions are true.

#Example 1:
#Input: n = 3
#Output: ["1","2","Fizz"]

#Example 2:
#Input: n = 5
#Output: ["1","2","Fizz","4","Buzz"]

#Example 3:
#Input: n = 15
#Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

def fizz_buzz(num):
    result = []
    for i in range(1,num+1):
        # Append "FizzBuzz" when the number is divisible by 15
        if i % 15 == 0: result.append("FizzBuzz")

        # Append "Fizz" when the number is divisible by 3
        elif i % 3 == 0: result.append("Fizz")

        # Append "Buzz" when the number is divisible by 5
        elif i % 5 == 0: result.append("Buzz")

        # Append the string form of the number
        # If all the above conditions does not satisfy
        else: result.append(str(i))
    
    return result

if __name__ == "__main__":
    test_cases = [3, 5, 15, 16, 6, 8]

    for num in test_cases:
        print(fizz_buzz(num))
