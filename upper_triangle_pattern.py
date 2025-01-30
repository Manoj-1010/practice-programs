def upper_triangle(symbol, rows):
  # The range should be from the number of rows, till 1, decreasing by 1 for each step
    for i in range(rows, 0, -1):
        print(symbol*i)

upper_triangle("*", 10)
