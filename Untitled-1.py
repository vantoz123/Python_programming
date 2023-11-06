# message = input("> ")
# words = message.split(" ")
# emojis = {
#     ">>":"😃",
#     "<<":"😣",
# } 
# output = ""
# for word in words:
#     output += emojis.get("! ", word) + " "
# print(output)

# values = [[3,4,5,1], [33,6,1,2]]
# x = values[0][0]
# for lst in values:
#     print(lst)
#     for element in lst:
#         print(element)
#         if x>element:
#             x = element
# print(x)

class Person:
    def __init__(self, name) -> None:
        self.name = name
        pass
    def talk(name):
        print("talk")
        pass

p1 = Person("Vantoz Kipz")
print(p1.name)
p1.talk()