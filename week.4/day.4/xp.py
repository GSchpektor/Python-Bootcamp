# Exercise 1

# def display_message():
# 	print("I am learning about functions in this exercise")

# Exercise 2

# def favorite_book(title):
# 	print(f"One of my favorite books is {title}")

# Exercise 3

# def increase(num):
# 	# total = []
# 	# # for i in range(1,5): # incrementing 4 times
# 	# # 	total.append(int(str(num)*i)) # num into string in order to concatenate num 

# 	return sum([int(str(num)*i) for i in range(1,5)] )

# print(increase(2))


# [int(str(num)*i) for i in range(1,5)] 


# Exercise 4

# def describe_city(city, country="Belgium"):
# 	print(f"{city} is in {country}")

# describe_city("Antwerp")
# describe_city("Brussels")
# describe_city("London", "UK")

# Exercise 5

# def make_shirt(size, text):
# 	print(f"You're shirt size is: {size} and has the following text: {text}")

# make_shirt("L", "Hello")
# make_shirt(text="Hello", size="L")

# def make_shirt(size="large", text="I love Python."):
# 	print(f"You're shirt size is: {size} and has the following text: {text}")

# make_shirt()
# make_shirt("medium")
# make_shirt("any size", "dif message")


# Exercise 6

# magician_names = ["Bob", "Bill", "Houdini"]

# def show_magicians(name):
# 	print(f"magician name is {name}")

# for names in magician_names:
# 	show_magicians(names)

# def make_great(show_magicians):
# 	print(f"{show_magicians} the great")

# for names in magician_names:
# 	make_great(names)


# Exercise 7

def get_age(year, month=1, day=1):
	current_date = [2020, 11, 11]
	age_year = current_date[0] - year
	return age_year

def can_retire(gender, date_of_birth):
	age = get_age(date_of_birth)
	if gender == "male":
		if age > 67:
			print("you can retire")
		else:
			print("you can't retire")
	if gender == "female":
		if age > 62:
			print("you can retire")
		else:
			print("you can't retire")
		

























