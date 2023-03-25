# write a python script to calculate sum of digits of a given number
num1=12345
num2=num1
sum=0
while(num2>0):
    r=num2%10
    sum+=r
    num2//=10
print("Sum=%d"%sum)