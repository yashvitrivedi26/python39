'''write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice using switch statements.
'''

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
op = input("Enter Operation(+,-,*,/):")

if op=='+':
    print("Addition is:",num1+num2)
elif op=='-':
    print('Subtraction is:',num1-num2)
elif op=='*':
    print('Multiplicatio is:',num1*num2)
elif op=='/':
    print('Division is:',num1/num2)
else:
    print('Enter Valid Operator')
