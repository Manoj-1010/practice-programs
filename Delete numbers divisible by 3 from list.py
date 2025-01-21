num=[i for i in range(1,11)] # Sample list with numbers
print('Original list: ',num) # Printing the unmodified list

# For loop for removal of multiples of 3 from the list
for x in num: 
    if x%3==0:
        num.remove(x)

# Final list is printed
print('Multiples of 3 is removed: ',num)
