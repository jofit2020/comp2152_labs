from Person import Person
class Student(Person):
    def __init__(self,name,age,height,major):
        super().__init__(name,age,height) # Call parent constructor
        self.major=major # New public property
        print("This time it's a Student object")

# Creating an instance of student
std=Student("Maria",22,6,"Computer Science")

# Checking attributes
print(std.name) # should print "Maria"
print(std.major) # should Print "Computer science"
