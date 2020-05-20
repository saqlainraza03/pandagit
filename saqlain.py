

#assignments faulty calculator
print("WELCOME TO CALCULATOR!!-DEVELOPED BY aloveras ")
print("CHOOSE THE OPERATION YOU HAVE TO PERFORM")

print("(1)SUM")
print("(2)SUBTRACT")
print("(3)MULTIPLY")
print("(4)DIVIDE")
num=int(input())
if num==1:
 print("ENTER TWO NUMBER TO FIND THE SUM")
 n1=int(input())
 n2=int(input())
 if n1+n2==56+9:
     print("THE SUM OF THE TWO NUMBERS IS:  77")
 else :
  print("THE SUM OF THE TWO NUMBERS IS: ",n1+n2)

if num==2:
     print("ENTER TWO NUMBER TO FIND THE SUBTRACTION")
     n1=int(input())
     n2=int(input())
     print("THE SUBTRACTION OF THE TWO NUMBERS IS: ",n1-n2)

if num==3:
    print("ENTER TWO NUMBER TO FIND THE MULTIPLY")
    n1=int(input())
    n2=int(input())
    if n1*n2==45*3:
        print("THE MULTIPLICATION OF THE NUMBERS IS: 555")
    else:
        print("THE MULTIPLICATION OF THE NUMBERS IS: ",n1*n2)

if num==4:
    print("ENTER TWO NUMBERS TO FIND DIVISION")
    n1=int(input())
    n2=int(input())
    if n1/n2==56/4:
        print("THE DIVISION OF THE NUMBER IS:  4")
    else:
        print("THE DIVISION OF THE NUMBERS IS: ",n1/n2)

