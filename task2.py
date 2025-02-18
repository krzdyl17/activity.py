class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("John", 22, "Information Technology")
student2 = Student("Dale", 24, "Architecture")
student3 = Student("Ryan", 20, "Agriculture")

student1.introduce()
print()
student2.introduce()
print()  
student3.introduce()
print()
