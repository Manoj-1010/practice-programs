# Function for printing numbers from first to last
def first_to_last(first, last):
    if first > last: print(-1); return # Return -1 if first is greater than last
    while first <= last: # Loop statement for printing the series
        print(first, end=" ")
        first += 1

if __name__ == "__main__":
    first_to_last(1,10) # Output: 1 2 3 4 5 6 7 8 9 10
    first_to_last(7,5) # Output: -1
