# Exercise 1
import random
import statistics

# def get_random_temp():
# 	temp = random.randint(-10,40)
# 	return temp

# def main():
# 	temperature = get_random_temp()
# 	if temperature < 0:
# 		print("Brrr, that’s freezing! Wear some extra layers today")
# 	if 0 <= temperature < 16:
# 		print("Quite chilly! Don’t forget your coat")
# 	if 16 <= temperature < 24:
# 		print("summer in England")
# 	if 24 <= temperature < 32:
# 		print("normal in Israel")
# 	if 32 <= temperature <= 40:
# 		print("Heatwave")

# def get_random_temp(season):
# 	if season == "winter":
# 		temp = random.randint(-10,16)
# 	if season == "autumn":
# 		temp = random.randint(17,22)
# 	if season == "spring":
# 		temp = random.randint(23,28)
# 	if season == "summer":
# 		temp = random.randint(29,40)
# 	return temp

# def main():
# 	user_input = input("select a season (winter, autumn, spring, summer)")
# 	temperature = get_random_temp(user_input)
# 	if temperature < 0:
# 		print("Brrr, that’s freezing! Wear some extra layers today")
# 	if 0 <= temperature < 16:
# 		print("Quite chilly! Don’t forget your coat")
# 	if 16 <= temperature < 24:
# 		print("summer in England")
# 	if 24 <= temperature < 32:
# 		print("normal in Israel")
# 	if 32 <= temperature <= 40:
# 		print("Heatwave")

# Exercise 2

def throw_dice():
	 dice_roll = random.randint(1,7)
	 return dice_roll

def throw_until_doubles():
	total_throws = 0
	while True:
		die_1 = throw_dice()
		die_2 = throw_dice()
		if die_1 != die_2:
			total_throws +=1
		if die_1 == die_2:
			total_throws +=1
			# print(total_throws)
			return total_throws
			break

def main():
	total_double_throws = 0
	average = []
	for _ in range(100):
		roll_result = throw_until_doubles()
		total_double_throws += roll_result
		average.append(roll_result)

	print(total_double_throws)
	print(statistics.mean(average))









