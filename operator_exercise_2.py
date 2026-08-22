'''write a program to display dinomations of currency for given amount
input : 387 Rupees 
output : 
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01
'''


amount = int(input("Enter amount: "))

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n2 = amount // 2
amount = amount % 2

n1 = amount // 1
amount = amount % 1

print("200 x", n200, "=", 200 * n200)
print("100 x", n100, "=", 100 * n100)
print("50 x", n50, "=", 50 * n50)
print("20 x", n20, "=", 20 * n20)
print("10 x", n10, "=", 10 * n10)
print("5 x", n5, "=", 5 * n5)
print("2 x", n2, "=", 2 * n2)
print("1 x", n1, "=", 1 * n1)