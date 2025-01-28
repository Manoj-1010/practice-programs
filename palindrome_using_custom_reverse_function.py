def isPalindrome(string):
    if string.lower() == reverse(string.lower()):
        print(f"{string.capitalize()} is a Palindrome.")
    else:
        print(f"{string.capitalize()} is not a Palindrome.")

def reverse(string):
    reverse = ""
    for i in range(len(string)-1, -1, -1):
        reverse += string[i]
    
    return reverse

if __name__ == "__main__":
    isPalindrome(input())
