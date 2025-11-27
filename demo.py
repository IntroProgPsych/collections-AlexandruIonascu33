fruits = ["orange", "apple", "banana"] # List of fruits
vegetables = {"carrot", "broccoli", "spinach"} # Set of vegetables
sweets = ("cake", "ice cream", "candy") # Tuple of sweets
date = {"day": 15, "month": "June", "year": 2024} # Dictionary representing a date

print(fruits,fruits[0])
print(vegetables)
print(sweets,sweets[1])
print(date,date["month"])

fruits[0] = "grape" # Modifying list element
print(fruits)
# vegetables[0] = "lettuce" # This would raise an error since sets are unordered
vegetables.add("lettuce") # Adding an element to the set
print(vegetables)
# sweets[1] = "pudding" # This would raise an error since tuples are immutable
date["day"] = 16 # Modifying dictionary value
print(date)
