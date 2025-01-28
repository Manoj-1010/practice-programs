def remove_special_characters(string):
    result = ""
    for _ in string:
        if _.isalnum(): # Checking if the given character is either an alphabet, or a number
            result += _ # Appending the character to the result string
    return result

if __name__ == "__main__":
    print(remove_special_characters(input("Enter the string: ")))
