def palindrome_number(num):
    reverse = 0
    temp = num
  # Multiply the value of the reverse by 10, and add the remainder of the number when divided by 10
    while temp != 0:
        reverse = reverse * 10 + (temp % 10)
        temp = temp // 10

  # Compare the original number and the reversed number
    if reverse == num: return True
    else: return False

if __name__ == "__main__":
    if palindrome_number(int(input())):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
