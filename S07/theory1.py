class Car:
    def __init__(self, brand, speed=0): #parameter of all methods, the object itself
        self.brand = brand #atribute
        self.speed = speed
        self.value = 0 #either 0, None or ""

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    """def speed(self):
        return 100"""

    def get_brand_nacionality(self):
        if self.brand == "Renault":
            return "France"
        elif self.brand == "Ferrari":
            return "Italy"

    def set_age(self, age):
        self.age = age

mycar = Car("Renault" , 30)
print(mycar.get_speed())
mycar.set_speed(80)
print(mycar.get_speed())

print(mycar.get_brand_nacionality())

yourcar = Car("Ferrari", 250)
print(yourcar.speed)
print(yourcar.get_speed())