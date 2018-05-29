#Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
#The Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
	#The Dog has-a name
		self.name = name
		
#The cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		#The cat has-a name
		self.name = name

#Person is-a object
class Person(object):
	def __init__(self, name):
		#Person has-a name
		self.name = name
		#Person has-a pet
		self.pet = None

#Employee is-a person
class Employee(Person):
	def __init__(self, name, salary):
		##??hm what is this strange magic?
		super(Employee, self).__init__(name)
		#Employee has-a salary.
		self.salary = salary
		
#Fish is-a object
class Fish(object):
	pass
	
#Salmon is-a fish 
class Salmon(Fish):
	pass
	
#Halibut is-a fish
class Halibut(Fish):
	pass
	
#rover is-a Dog
rover = Dog("Rover")

#Satan is-a cat
satan = Cat("Satan")

#Mery is-a Person
mary = Person("Mary")

#Mery has-a pet named Satan
mary.pet = satan

#Frank is-a employee
frank = Employee("Frank", 120000)

#Frank has-a pet named Rover
frank.pet = rover

#Flipper is-a fish
flipper = Fish()

#Crouse is-a Salmon
crouse = Salmon()

#Harry is-a Halibut
harry = Halibut()