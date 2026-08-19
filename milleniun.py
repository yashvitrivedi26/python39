#write a program to findout whether given year is millennium year or not. using if else decision making statements.

yr = int(input("Enter Year:"))

if yr % 1000==0:
    print("It is a Millenium Year")
else:
    print("It is not a Millenium Year")