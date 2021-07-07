#Inheritance is when we create a class from class already created

class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def whoami(self):
        print("I'M AN ANIMAL")

    def eat(self):
        print("I am EATING!")

class dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def whoami(self):
        print("I'm a DOG!")

mydog = dog()
mydog.whoami()


#POLYMORPHISM
class ddog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says WHOOF WHOOF!!"

class cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says MEOWWW!!"


#Abstract