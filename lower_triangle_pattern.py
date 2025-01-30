def lower_triangle(symbol, rows):
  # Print the symbol from 1 till the given number, each times incrementing the count by one
    for i in range(rows):
        print(symbol*(i+1))

if __name__ == "__main__":
    lower_triangle("*", 5)
