def reverse_string(string):
    reverse = ""
    # Create a for loop which goes in reverse from the length of the string to the start of the string
    for i in range(len(string)-1, -1, -1):
        reverse += string[i] # Concatenate the character at the given index to the reverse string
    
    return reverse

if __name__ == "__main__":
    print(reverse_string(input()))
