# a function that illustrates that an object can have functions/methods in it

class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass

    def Myfunc(self):
        print("Hello my name is "+ self.name)

p1 = person("John", 36)
p1.Myfunc()