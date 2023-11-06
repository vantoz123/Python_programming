class Student:
    def __init__(self, name, major, gpa, is_on_probation) -> None:
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

        pass
    def __str__(self) -> str:
        return f"{self.name} {self.major} {self.gpa} {self.is_on_probation}"
        
        pass