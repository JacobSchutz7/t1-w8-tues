from abc import ABC, abstractmethod
import math

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius ** 2
	
	def perimeter(self):
		return 2 * math.pi * self.radius

class Rectangle(Shape): 
	def __init__(self, length, width):
		self.length = length
		self. width = width

	def area(self):
		return self.length * self.width
	
	def perimeter(self):
		return 2 * (self.length + self.width)

circ = Circle(3)
rect = Rectangle(4, 7)

print(circ.area())
print(circ.perimeter())
print(rect.area())
print(rect.perimeter())