# Mammal Class
from heart import Heart
class Mammal:
    def __init__(self,age):
        self.__age=age
        self.heart_obj=Heart()

    def speak(self):
        print("Mammal makes sound Woooo!")

    def __str__(self):
        return f"Mammal is {self.__age} years old"
