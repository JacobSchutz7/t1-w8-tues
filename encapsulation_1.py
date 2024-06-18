class Person:
	def __init__(self, name, age, email):
		self.name = name
		# two private variables
		self.__age = age
		self.__email = email

	# getter function - age
	def get_age(self):
		return self.__age
	# setter function - age
	def set_age(self, age):
		self.__age = age
	# getter function - email
	def get_email(self):
		return self.__email
	# setter function - email
	def set_email(self, email):
		self.__email = email
	
	def display_info(self):
		return f"Name: {self.name}, Age: {self.__age}, Email: {self.__email}"
	
Jim = Person("Jim", 27, "jim@mail.com")

print(Jim.get_email())
Jim.set_email("jimtime@mail.com")
print(Jim.get_email())