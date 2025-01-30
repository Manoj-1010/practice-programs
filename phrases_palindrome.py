def phrase_palindrome(phrase):
    # Two pointers, left and right will keep track of the valid characters
    left, right = 0, len(phrase) - 1

    while left < right:
        # If the character at current is not alpha numeric,
        # We update the counters by moving inward
        if not phrase[left].isalnum():
            left += 1
            continue

        if not phrase[right].isalnum():
            right -= 1
            continue

        # We check if the valid characters are equal, irrespective of their case
        # They will be equal if the phrase is Palindrome
        # If not, we return False
        if phrase[left].lower() != phrase[right].lower(): return False

        right -= 1
        left += 1
    
    return True

if __name__ == "__main__":
    test_cases = [
    "A man, a plan, a canal: Panama", 
    "race a car",                     
    " ",                              
    "No 'x' in Nixon",                
    "Was it a car or a cat I saw?",  
    "123321",                         
    "123456",                           
    "abccba",                          
    "abcdba",                           
    "Able , was I saw eLba!" ]

    for phrase in test_cases:
        if phrase_palindrome(phrase): print("It is a Palindrome!")
        else: print("It is not a Palindrome!")
