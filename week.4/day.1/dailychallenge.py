string = input("string of 10 characters")
if len(string) > 10:
	print("you're string is too long")
elif len(string) < 10:
	print("you're string is too short")
else:
	print(string[0], string[-1])

for i in range(len(string)):
	print(string[0:i+1])

import random
print("original string: ", string)
final_str = "".join(random.sample(string, len(string)))
print("shuffled string is: ", final_str)

