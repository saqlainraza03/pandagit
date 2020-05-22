#pattern using for and type casting boolean

n=int(input("enter a number"))
a= int(input("enter your boolean number"))
if bool(a):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("$",end="")
        print()
else:
    for i in range(1,n+1):
        for j in range(1,n+2-i):
            print("*",end="")
        print()