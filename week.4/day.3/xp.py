# Exercise 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# numbers = zip(keys, values)
# print(dict(numbers))

# Exercise 2 

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total = 0

# for name, age in family.items():
# 	if age>3 and age <12:
# 		print(f"{name} has to pay $10")
# 		total += 10
# 	elif age >= 12:
# 		print(f"{name} has to pay $15")
# 		total += 15

# print(total)

# customers = {}
# total = 0

# while True:
# 	name = input("What's your name ")
# 	if name == "x":
# 		break
# 	age = int(input("What's your age "))
# 	customers[name] = age

# for name, age in customers.items():
# 	if age>3 and age <12:
# 		print(f"{name} has to pay $10")
# 		total += 10
# 	elif age >= 12:
# 		print(f"{name} has to pay $15")
# 		total += 15

# Exercise 3

# brand = {
# 	"name": "Zara",
# 	"creation_date": 1975,
# 	"creator_name": "Amancio Ortega Gaona", 
# 	"type_of_clothes": ["men", "women", "children", "home"],
# 	"international_competitors": ["Gap", "H&M", "Benetton"], 
# 	"number_stores": 7000,
# 	"major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
# }

# brand["number_stores"] = 2

# print(f"The clients of Zara are: {' '.join(brand['international_competitors'])}")

# brand["country_creation"] = "Spain"

# brand["international_competitors"].append("Desigual")

# brand.pop("creation_date")

# print(brand["international_competitors"][-1])

# print(', '.join(brand["major_color"]["US"]))

# print(len(brand.keys()))

# print(brand.keys())

# more_on_zara = {
# 	"creation_date": 1975, 
# 	"number_stores": 10000 
# }

# brand.update(more_on_zara)

# print(brand)

# print(brand["number_stores"])

# it overrided it

# Exercise 4

# users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"] 
# users2 = {}

# for number, name in enumerate(users):
# 	users2[name] = number

# print(users2)

# users2 = {}

# for number, name in enumerate(users):
# 	users2[number] = name

# print(users2)

# users2 = {}
# users.sort()
# for number, name in enumerate(users):
# 	users2[name] = number

# print(users2)

# users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"] 
# users2 = {}

# for number, name in enumerate(users):
# 	if name.find("i") == -1:
# 		continue
# 	users2[name] = number

# print(users2)

users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"] 
users2 = {}

for number, name in enumerate(users):
	if name.index("N") == True:
		continue
	users2[name] = number

print(users2)









