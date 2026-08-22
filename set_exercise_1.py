'''create two list fruits and vegis (both might have duplicate values) 
convert both list into single set refrigerator 
'''

fruits = ["Apple", "Mango", "Banana", "Apple", "Orange"]
vegis = ["Potato", "Tomato", "Carrot", "Potato", "Onion"]

refrigerator = set(fruits + vegis)

print("Refrigerator:", refrigerator)