'''write a program to convert given grams into kg and remaining grams.
input : 2500 grams
output : 2 kg and 500 grams 
'''

grams = int(input("Enter grams: "))

kg = grams // 1000
remaining_grams = grams % 1000

print(kg, "kg and", remaining_grams, "grams")