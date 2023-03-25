# write a python script to  print  the octal equivalent of  a given decimal number(do not use oct() method)
num=int(input("enter the number"))
l=[]
while(num>0):
    r=num%8
    l.append(str(r))
    num//=8
l.reverse()
octal="".join(l)

print("octal is {}".format(octal))