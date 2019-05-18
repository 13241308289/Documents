# -*- encoding: utf-8 -*-

# ##################简单工厂#####################


class Animal:
	# 动物的类定义
	def __init__(self, name):
		self.name = name


class Dog(Animal):
	# 小狗类，具有bark方法
	def __init__(self, name):
		Animal.__init__(self, name)
	
	def bark(self):
		print "I'm %s, 汪汪汪！" % self.name


class Cat(Animal):
	# 小猫类，具有bark方法
	def __init__(self, name):
		Animal.__init__(self, name)
	
	def bark(self):
		print "I'm %s, 喵喵喵！" % self.name


def simple_factory(animal_type, animal_name):
	# 简单工厂
	if animal_type == "dog":
		animal = Dog
	elif animal_type == "cat":
		animal = Cat
	else:
		raise ValueError('Unknow animal!')
	
	return animal(animal_name)


def main():
	dog = simple_factory('dog', 'Tom')
	cat = simple_factory('cat', 'Jerry')
	dog.bark()
	cat.bark()


if __name__ == '__main__':
	main()
