'''write a program to findout which is cheaper approach to buy IPhone 17 pro max.  consider user is going usa should he buy 
iphone from usa or from india. take required input from user and suggest from where he should buy i-phone (india or USA)'''

usa_price = int(input("Enter USA IPhone Price in Dollar:"))
ind_price = int(input("Enter India IPhone Price in Rupee:"))
rupee = int(input("Enter Rupee per Dollar:"))


u_price = usa_price * rupee
print("USA Price in Rupee:",u_price)
print("Indian Price in Rupee:",ind_price)
if u_price>ind_price:
    print("He should buy IPhone from India")
else:
   print("He should buy IPhone from USA") 