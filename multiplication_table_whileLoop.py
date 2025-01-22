# Function to generate the multiplication table
def multiplication_table(n, s): # Args: n = Multiplicant; s = Multiplier limit
    i = 1
    while i <= s: # While loop for generating the multiplication table
        print(f"{n} x {i} = {n*i}")
        i += 1

if __name__ == "__main__":
    # Getting user inputs for 'n' and 's'
    n = int(input("Enter the Multiplicant: "))
    s = int(input("Enter the Multiplier limit: "))
    
    multiplication_table(n,s)
