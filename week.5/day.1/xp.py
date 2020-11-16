# Exercise 1

# class Cat:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# cat1 = Cat("Pitsie", 2)
# cat2= Cat("Rafi", 1)
# cat3 = Cat("Hairy", 3)

# def oldest(cat1, cat2, cat3):
# 	cats = [cat1, cat2, cat3]

# 	oldest = cats[0]
# 	for cat in cats:
# 		if cat.age > oldest.age:
# 			oldest = cat

# 	print(f"The oldest cats is {oldest.name}, it is {oldest.age} old")

# Exercise 2

# class Dog:

# 	def __init__(self, name, height):
# 		self.name = name
# 		self.height = height

# 	def bark(self):
# 		print(f"{self.name} goes woof!")

# 	def jump(self):
# 		print(f"{self.name} jumps {self.height*2} cm high!")

# davids_dog=Dog("rex", 50)
# sarahs_dog=Dog("Teacup", 20)

# if davids_dog.height > sarahs_dog.height:
# 	print(f"{davids_dog.name} is bigger")
# else:
# 	print(f"{sarahs_dog.name} is bigger")


# Exercise 3

# class Song:

# 	def __init__(self, lyrics):
# 		self.lyrics = lyrics

# 	def sing_me_a_song(self):
# 		for lyric in self.lyrics:
# 			print(lyric)
# 			print("\n")

# stairway=["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]


# Exercise 4

class Zoo:

	def __init__(self, zoo_name):
		self.zoo_name=zoo_name
		self.name = zoo_name
		self.animals = []
		self.sorted_animals={}

	def add_animal(self, new_animal):
		self.new_animal=new_animal

		if self.animals.count(new_animal) == 0:
			self.animals.append(new_animal)
		else:
			print(f"{new_animal} already in zoo")

	def get_animals(self):
		print(self.animals)

	def sell_animal(self, animal_sold):
		self.animal_sold=animal_sold
		if self.animals.count(animal_sold) > 0:
			self.animals.remove(animal_sold)

	def sort_animals(self):
		self.animals.sort()

		key = 1
		letter = self.animals[0][0]

		for animal in self.animals:
			if animal[0] != letter:
				key += 1
				letter = animal[0]

			if key in self.sorted_animals:
				if not isinstance(self.sorted_animals[key], list):
					self.sorted_animals[key] = [self.sorted_animals[key]]
				self.sorted_animals[key].append(animal)
			else:
				self.sorted_animals[key] = animal

	def get_groups(self):
		if not self.sorted_animals:
			self.sort_animals()

		for item in self.sorted_animals.items():
			print(item)

ramat_gan_safari = Zoo(ramat_gan_safari)





















