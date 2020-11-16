class Farm:

	def __init__(self, name):
		self.name=name
		self.animals ={}
		self.sorted_types=[]

	def add_animal(self, animal_name, amount):
		self.animal_name=animal_name
		self.amount=amount
		self.animals[self.animal_name]=self.amount

	def song(self):
		print(f"{self.name} had a farm \n")
		print("E-I-E-I-O!")
		for item in self.animals.items():
			print(f"{item}\n")

	def get_animal_types(self):
		self.sorted_types.append(sorted(self.animals.keys()))
		return self.sorted_types

	def get_short_info(self):
		for item in self.sorted_types:
			item =  str(item, ",")

		print(f"{self.name}'s farm has {self.sorted_types}")