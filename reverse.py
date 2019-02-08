i=int(input("Enter a number"))
sum=0
while (i>1):
    n=int(i%10)
    sum=sum*10+n
    i=int(i/10)
print (sum)    