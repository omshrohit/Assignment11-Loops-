# write a python script to calculate sum of square of first N natural numbers
n=int(input("enter the value of  n"))
sum=0
for i in range(1,n+1):
    sum+=i**2
print(f"result is {sum}")