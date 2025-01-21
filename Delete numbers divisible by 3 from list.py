num=[i for i in range(1,11)]
print('Original list: ',num)
for x in num:
    if x%3==0:
        num.remove(x)
print('Multiples of 3 is removed: ',num)