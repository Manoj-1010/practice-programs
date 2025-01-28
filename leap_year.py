def checkYear(n):
    # Check if n is divisible by 4
    if n % 4 == 0:
        # If it's divisible by 100, it should also be divisible by 400 to be a leap year
        if n % 100 == 0:
            return n % 400 == 0
        return True
    return False

if __name__ == "__main__":
  year = int(input("Enter the year: "))
  if checkYear(year):
      print(f"{year} is a leap year")
  else:
      print(f"{year} is not a leap year")
