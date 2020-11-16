


import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
shown_word = ["*"*len(word)]
gallows = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

guessed_letters = [] 


def guess_word():       
	letter = input("guess a letter")
	if word.count(letter) > 0:
		position = word.index(letter)
		shown_word.pop(position)
		shown_word.insert(position, str(letter))
		print(shown_word)
		guessed_letters.append(str(letter))
	else:
		guessed_letters.append(str(letter))
		gallows.pop(-1)
		print("you have just lost a life")
	print(f"These are the letters which have been guessed {guessed_letters}")
	print(f"the gallows consist of {gallows}")





# def guessed_already(): 
# 	if guessed_letters.count(letter) > 0:
# 		return True
# 	else: 
# 		return False


def play(): 
	print(word)
	print(shown_word)

	while len(gallows) > 0:
		guess_word()
		print(shown_word)
	print("Game over")



