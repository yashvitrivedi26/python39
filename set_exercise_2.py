'''assume there are two list friends and families both have 10 mobile numbers. it is quite possible that both list have same 
numbers. you job is to create telephone_directory which must not contain any duplicate number using set '''

# Create two lists of mobile numbers

friends = [
    "9876543210",
    "9876543211",
    "9876543212",
    "9876543213",
    "9876543214",
    "9876543215",
    "9876543216",
    "9876543217",
    "9876543218",
    "9876543219"
]

families = [
    "9876543210",
    "9876543221",
    "9876543222",
    "9876543223",
    "9876543224",
    "9876543225",
    "9876543226",
    "9876543227",
    "9876543228",
    "9876543229"
]

telephone_directory = set(friends + families)

print("Telephone Directory:", telephone_directory)