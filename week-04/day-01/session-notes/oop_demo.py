from typing import override

class Student:
    def __init__(self, name, age, major) -> None:
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f'Hi, I am {self.name}, a {self.age} year old {self.major} major'

    def hi(self):
        return f"Hi, I am {self.name}. I am exciteeeed!"

# -------------------------------------------------------------------- #

s1 = Student('Alice', 20, 'CS')
s2 = Student('Michael', 22, 'Biology')

# print(s1.hi())
print(s2.introduce()) # - prints: Hi, I am Michael, a 22 year old Biology major

# Inheritance: TeachingFellow class is a subclass of Student
# The idea is to have this TeachingFellow class inherit everything from its parent class (Student)
class TeachingFellow(Student):
    def __init__(self, name, age, major, cohort):
        # Call the super class (Student) to initialize the given fields into it
        super().__init__(name, age, major)
        self.cohort = cohort

    # override the introduce function from its Student parent class: changes its behavior so that objects that
    # belong to TeachingFellow call this introduce function defined in TeachingFellow instead of the function from Student
    @override
    def introduce(self):
        return f"{super().introduce()}. I am also TF-ing {self.cohort}"

tf = TeachingFellow('Michelle', 19, 'Physics', 'Summer 2026')
print(tf.name) # - prints: Michelle

# Calls introduce function from the parent class
print(tf.introduce()) # - prints: Hi, I am Michelle, a 19 year old Physics major
