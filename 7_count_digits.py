# write a python script to count digits in a given number
num1=1240
count=0
num2=num1

while(num2>0):
    count+=1
    num2//=10
print("number of digit is %d"%count)



# another way
'''
num1=123445
num2=str(num1)
print(len(num2))

'''