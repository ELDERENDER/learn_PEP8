class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        self.weight += food
        return self.weight

    def info(self):
        print(f"{self.name}, {self.age} years, {self.weight} kg")


class Cat(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def bark(self):
        print("MEOW!")


def validate_age(age):
    if 0 <= age <= 150:
        if age < 18:
            return "minor"
        elif 18 <= age < 65:
            return "adult"
        else:
            return "senior"
    else:
        return "invalid"


x = 10
y = 20
z = 30
if x < y < z:
    print("Increasing sequence")
