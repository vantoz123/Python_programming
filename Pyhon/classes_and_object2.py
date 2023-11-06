#using the _init_() function
#is an inbuilt function that is always executed when class is initiated
# we use the _init_() function if we want to assign values to object properties or other operations that are necessary to do when the object is being created

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John", 24)
print(p1.name)
print(p1.age)