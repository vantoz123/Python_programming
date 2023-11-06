# using the _srt_() function.
#1 Without _str_() function
'''
class person:
    def __init__(properties,name,age):
        properties.name = name
        properties.age = age
p1 = person("John", 36)
print(p1)
'''

# to solve the issues in the code above use the _str_() function

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(properties):
        return f"My name is {properties.name} and i am ({properties.age}) years old."
    
p1  = person("Vantoz", 22)
print(p1)