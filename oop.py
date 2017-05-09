"""

# inheritance: The ability to create subclasses that mimic parent class in terms of data and behaviors
# polymorphism: Ability to overload standard operators so that they have appropriate behaviors based on their context
# encapsulation: dividing code into public interface and a private implementation on that interface

"""
class Drink(object):
	def describe(self):
		return "Drink"

	def cost(self):
		return 0.0

class Coffee(Drink):
	def describe(self):
		return "It's normal coffee"

	def cost(self):
		return 20

class Tea(Drink):
	def describe(self):
		return "It's tea"

	def cost(self):
		return 25

class CoffeWithMilk(Coffee):
	def describe(self):
		return super(CoffeWithMilk, self).describe + ", with milk"

	def cost(self):
		return super(CoffeWithMilk, self).cost + 10

	
		
		
