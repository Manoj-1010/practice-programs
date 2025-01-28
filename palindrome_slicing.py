def isPalindrome(string):
    # Comparing the original string, and it's reversed string, we can determine if it is a Palindrome or not
    if string.lower() == string[::-1].lower():
        print(f"{string.capitalize()} is a palindrome")
    else:
        print(f"{string.capitalize()} is not a palindrome")

if __name__ == "__main__":
    isPalindrome(input())
