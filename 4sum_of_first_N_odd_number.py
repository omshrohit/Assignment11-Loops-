# write a python script to  calculate sum of first N odd natural numbers
n=int(input("enter the value of n"))
sum=0
for i in range(1,n*2,2):
    sum+=i
print(f"sum is {sum}")