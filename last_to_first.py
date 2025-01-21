# Function for printing numbers from last to first
def last_to_first(last, first):
    if last < first: print(-1); return # Return -1 if last is lesser than first
    while last > 0: # Loop statement for printing the series
        print(last, end=" ")
        last -= 1

last_to_first(8,2) # Output: 8 7 6 5 4 3 2
print()
last_to_first(1,6) # Output: -1
