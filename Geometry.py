#WAP to enter length and width and check if the shape is square,landscape or potrait using if statement

len = int(input("Enter Length:"))
width = int(input("Enter Width:"))

if(len==width):
    print("It is a Square")
if(len<width):
    print("It is a Landscape")
if(len>width):
    print("It is a Potrait")