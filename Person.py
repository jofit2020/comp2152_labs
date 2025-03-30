from mammal import Mammal
class Person(Mammal):

        def __init__(self,name,age,height):
            self.__name=name  # Double underscore __name makes it private
            self.__age=age
            self.__height=height
            self.public_prop="I'm public"
            print("Constructing the Person Object")
            super().__init__(age)

        def speak(self):
            print("Person Hello")

        def __str__(self):
            return f"Name: {self.__name} Heart rate {super().heart_obj.bpm}"

# Getter
        def get_name(self):
            return self.__name
# Setter
        def set_name(self,name):
            self.__name=name
# Magic getter for name
        @property
        def name(self):
            return self.__name
# Magic setter for name
        @name.setter
        def name(self,name):
            self.__name=name

        def __del__(self):
            print("The garbage collector is automatically destroying the Person Object")

p1=Person("Mark",20,6)
# print(p1.height) # Doesn't work
# Attempting to print private property directly (should cause an error)
try:
    print(p1.name) # Doesn't work
except AttributeError as e:
    print(f"Error: {e}")

# Attempting to to print p1.public_group or public field will work
# print(p1.public_prop) # This should work
#
# #Accessing private name using getter and setter
#
# print(p1.get_name()) # Expected output: "Anna"
# p1.set_name("Anna")
# # using magic getter and setter
# print(p1.name) # Expected output: "Anna"
# p1.name="John"
# print(p1.name) # Expected output: "John"
