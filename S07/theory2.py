class Vehicle:
    def set_speed(self, speed):
        self.speed = speed
class Car(Vehicle):
    def __init__(self, brand, speed=0): #parameter of all methods, the object itself
        self.brand = brand #atribute
        self.speed = speed

class Ferrari(Car): #mirar el init de car (brand es obligatorio)
    def __init__(self):
        #call the init of the mother class, para que se runee tmb:
        super().__init__("Ferrari", 100) #para que tmb runee el init de la mother class
        self.music = "classic" #adding extra info in this class, including what i had in the other classes
    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "Wow"

mycar = Car("Renault")
yourcar = Ferrari() #se quita el "Ferrari" de dentro del parentesis pq hemos añadido un init en su clase
print(yourcar.brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "and music is" , yourcar.music, "and speed is", yourcar.speed)

#print(mycar.make_cabrio(), "and music is" , mycar.music, "and speed is", mycar.speed) ERROR (bc of inheritance)