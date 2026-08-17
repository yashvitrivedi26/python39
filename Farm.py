#WAP to check which of the two farms is bigger using if statement

len1 = int(input("Enter Length of the Farm 1:"))
width1 = int(input("Enter Width of the Farm 1:"))

len2 = int(input("Enter Length of the Farm 2:"))
width2 = int(input("Enter Width of the Farm 2:"))

area1 = len1 * width1
area2 = len2 * width2

if(area1<area2):
    print("Farm 2 is bigger")
if(area1>area2):
    print("Farm 1 is bigger")

