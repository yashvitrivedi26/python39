'''create a list to store your favorite destination in india
create a list & store 10 different type of values in it 
    print all values 
    print 1st value 
    print 1st five value 
    print last 5 value 
    print list twice using * 
    print item in the list from 2nd to 5th position
    print count of items in list '''

destinations = ["Varkala", "Kedarnath", "Sikkim", "Kerala", "Udaipur", "Kashmir"]

print("Favorite Destinations:", destinations)

lst = ["Yashvi", 21, 85.5, True, "Python", 100, 3.14, False, "India", 500]

print("All values:", lst)

print("1st value:", lst[0])

print("1st five values:", lst[:5])

print("Last 5 values:", lst[-5:])

print("List twice:", lst * 2)

print("2nd to 5th position:", lst[1:5])

print("Count of items:", len(lst))