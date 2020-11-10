# Exercide 1

# my_fav_numbers = {7, 18}
# print(list(my_fav_numbers).pop(1))
# # my_fav_numbers = list(my_fav_numbers).pop(1)

# friend_fav_numbers = {1, 2, 3, 4}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# Exercise 2

# no


# Exercise 3

# for item in range(1, 21):
# 	print(item)

# Exercise 4

# 1. float has a decimal 
	
# for item in range(15, 46, 5):
# 	decimal = item / 10
# 	print(decimal)

# Exercise 5

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# first = basket.pop(0)
# print(basket)
# last = basket.pop()
# print(basket)
# basket.append("kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# Exercise 6

# while True:
# 	name = input("whats your name?")
# 	if name == "Guillaume":
# 		break
	
# Exercise 7

# numbers = list(range(0, 21))
# i = 0

# while i <= 21:
# 	if  i%2 == 0:
# 		print(numbers[i])
# 	i +=1

# Exercise 8

# for i in range(3, 31, 3):
# 	print(i)

# Exercise 9

# for i in range(1500, 2701):
# 	if (i%7 == 0) and (i%5 == 0):
# 		print(i)

# Exercise 10

# fruits = input("fav fruit or fruits with space in between ")
# fav_fruits = fruits.split()
# print(fav_fruits)


# ask = input("name a fruit")

# if fav_fruits.count(ask) >= 1:
# 	print("you picked one of your faves enjoy!")
# else:
# 	print("not one of faves, hope you like it") 

#bonus

# if len(fav_fruits) > 1:
# 	print(f"{fav_fruits[0:-1]}, and {fav_fruits[-1]}")


# Exercise 11

# toppings = []

# while True:
# 	pizza = input("input pizza topping, when finshed write quit")
# 	if pizza.lower() != "quit":
# 		print(f"i'll add {pizza} to you're pizza")
# 		toppings.append(pizza)
# 	else:
# 		total = 10 + (2.5*len(toppings))
# 		print(f"You're toppings are {toppings}, and you're total is {total}")
# 		break


# Exercise 12

# price = 0
# while True:
#     user_input = input("What is your age? ")
#     if user_input == "quit":
#         print(price)
#         break
#     else:
#         age = int(user_input)
#         if age>3 and age <12:
#             price += 10
#         elif age >= 12:
#             price += 15 


# allowed = []

# while True:
# 	user_input = input("What is your age? ")
# 	if user_input == "quit":
# 		print(allowed)
# 		break
# 	elif int(user_input) >= 16 and int(user_input) <= 21:
# 		name = input("Whats your name? ")
# 		allowed.append(name)



# Exercise 13













