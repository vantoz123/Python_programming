class Person:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("john", 34)
x.printname()

class Student(Person):
    def __init__(self, fname, lname, graduation) -> None:
        super().__init__(fname, lname)
        self.graduation = graduation

    def welcome(self):
        print("Hello", self.firstname, self.lastname, "to the class of ", self.graduation)
        ...
x = Student("mike", "Kosgei ",2020)

x.printname()
print(x.graduation)
x.welcome()

# print(x.graduation)