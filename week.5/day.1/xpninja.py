class Phone:

	def __init__(self, number):
		self.number=number
		self.call_history=[]
		self.messages=[]

	def call(self, other_phone):
		self.other_phone=other_phone
		self.call_history.append(self.other_phone)

	def show_call_history(self):
		print(f"your call history: {self.call_history}")

	def send_message(self, to_who, from_who, content):
		self.to_who=to_who
		self.from_who=from_who
		self.content=content

		self.message = {
			"To":to_who,
			"From":from_who,
			"Content":content
		}
		self.messages.append(self.message)

	def show_outgoing_messages(self):
		for message in self.messages:
			if self.from_who == self.number:
				print(f"Outgoing messages {message}")
			else:
				print("No outgoing messages")

	def show_incoming_messages(self):
		for message in self.messages:
			if self.from_who != self.number:
				print(f"Incoming messages {message}")
			else:
				print("No new messages")

	def show_messages_from(self, number):
		for message in self.messages:
			print(f"Message received from {self.messages[message]}")



