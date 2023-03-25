# write a python script to calculate binary Equivalent of a dicimal number(do not use bin() method)
num=int(input("enter a number"))
num2=num
l=[]
while(num2>0):
    r=num2%2
    l.append(str(r))
    num2//=2
l.reverse()
binary="".join(l)

print(binary)
