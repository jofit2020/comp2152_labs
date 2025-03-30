# Class Heart
# from mammal import Mammal
class Heart:
    def __init__(self):
        self.bpm=72
    def beat(self):
        print("Lub-dub")
        #update bpm
    def change_bpm(self):
        self.bpm=80
    def __str__(self):
        return f"Mammal is {self.bpm} years old"
