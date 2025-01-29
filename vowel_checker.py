def vowel_checker(char):
    vowel = "aeiouAEIOU"
  # Check if the given character is present in the string of vowel characters
  # Both in uppercase and lowercase
    if char in vowel: return True
    else: return False

if __name__ == "__main__":
    test_cases = ['z', 'G', 'E', 'o', 'P', '&', '2']
# Validating with custom test cases
    for char in test_cases:
        if vowel_checker(char):
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is not a vowel.")
