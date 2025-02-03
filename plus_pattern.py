def plus_pattern(index):
    for i in range(index):
        for j in range(index):
            
            # If the value of i or j
            # Is equal to the middle term, then print '*'
            #Ex: Middle term for 5 is 2 (since indexing starts from 0: 0 1 2 3 4)
            if i==(index-1)//2 or j==(index-1)//2: print("*", end=" ")
            
            # Else print empty space
            else: print(" ", end=" ")
        print()

if __name__ == "__main__":
    plus_pattern(5)
