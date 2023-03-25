# write a python script to calculate sum of first N even natural numbers
n=int(input("enter the value of n"))
sum=0
for i in range(2,n*2+1,2):
    sum=sum+i
print("result is {}".format(sum))