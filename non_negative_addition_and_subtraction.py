'''
You have two numbers, and your challenge is to write a program that performs both 
addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final 
results?

For example, consider two numbers 20 and 15. 
Addition of 2 values: 20 + 15 = 35.
Subtraction of 2 values: 20 - 15 = 5. 

For example, consider two numbers 20 and -150. 
Addition of 2 values: 20 + (-150) = -130 Absolute value of (-130) = 130.
Subtraction of 2 values: 20 - (-150) = 170.
'''

def add_and_subtract(num1, num2):
    print(
        f'''
Addition of 2 values: ({num1}) + ({num2}) = {abs(num1+num2)}.
Subtraction of 2 values: ({num1}) - ({num2}) = {abs(num1-num2)}.
        '''
    )

if __name__ == "__main__":
    a, b = map(int, input().split())
    add_and_subtract(a,b)