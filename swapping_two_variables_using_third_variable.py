def swap_values(num1, num2):
    print(f"Before swapping: {num1=} and {num2=}\n")
  # Assign the value of one number to the temporary variable, and interchange the values of variables num1 and num2.
    temp = num1
    num1 = num2
    num2 = temp
    print(f"After swapping: {num1=} and {num2=}\n")

if __name__ == "__main__":
    a, b = map(int, input().split())
    swap_values(a,b)
