# write a python script to calculate sum of first N natural numbers
n=int(input("enter the value of n"))
sum=0
for i in  range(1,n+1):
    sum+=i
print("sum of first %d number is %d"%(n,sum))