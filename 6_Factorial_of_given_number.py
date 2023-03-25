# write a python script to calculate factoraial of a given number.
n=int(input("enter the value of n"))
fac=1
for i in  range(n,0,-1):
    fac*=i
print("factorial is {}".format(fac))