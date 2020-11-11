# Exercise 1

# birthdays = {
# 	"Guillaume": "1993/10/15",
# 	"Devora": "1995/08/04",
# 	"Ezri": "2017/01/25",
# 	"Yael": "2018/12/19",
# 	"Alex": "1990/09/11"
# }

# print("welcome! You can look up the birthday of the people in the list!")

# user_input = input("name? ")

# print(f"Remember that {user_input} has a birthday on {birthdays[user_input]}")

# Exercise 2

# birthdays = {
# 	"Guillaume": "1993/10/15",
# 	"Devora": "1995/08/04",
# 	"Ezri": "2017/01/25",
# 	"Yael": "2018/12/19",
# 	"Alex": "1990/09/11"
# }

# print(f"welcome! You can look up the birthdays of: {birthdays.keys()}")

# user_input = input("name? ")
# if user_input in birthdays:
# 	print(f"Remember that {user_input} has a birthday on {birthdays[user_input]}")
# else:
# 	print(f"Sorry we don't have birthday information for {user_input}")

# Exercise 3

# birthdays = {
# 	"Guillaume": "1993/10/15",
# 	"Devora": "1995/08/04",
# 	"Ezri": "2017/01/25",
# 	"Yael": "2018/12/19",
# 	"Alex": "1990/09/11"
# }

# user_name = input("name: ")
# user_dob = input("DOB (YYYY/MM/DD): ")

# birthdays[user_name] = user_dob

# print(f"welcome! You can look up the birthdays of: {birthdays.keys()}")

# user_input = input("name? ")
# if user_input in birthdays:
# 	print(f"Remember that {user_input} has a birthday on {birthdays[user_input]}")
# else:
# 	print(f"Sorry we don't have birthday information for {user_input}")


# Exercise 4

# items = {
# 	"banana": 4,
# 	"apple": 2,
# 	"orange": 1.5,
# 	"pear": 3
# }

# print(items.items())
# for inventory in items:
# 	print(f"We have {items[inventory]} of {inventory}")

# stock = {
# 	"banana": 10,
# 	"apple": 25,
# 	"orange": 3,
# 	"pear": 7
# }

# Total = []
# for price in stock:
# 	Total.append(stock[price] * items[price])
# 	print(sum(Total))

# Exercise 5

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
print(cars)
cars_list = cars.split(",")

print(cars_list)

print(f"There are {len(cars_list)}")










