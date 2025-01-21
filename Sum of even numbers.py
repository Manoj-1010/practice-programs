num=[i for i in range(1,11)]
even=[]
print("ORIGINAL LIST: ",num)
for j in num:
    if j%2==0:
        even.append(j)
print("THE SUM OF EVEN NUMBERS IN THE LIST: ",sum(even))

