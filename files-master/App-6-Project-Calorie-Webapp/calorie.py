from temperature import Temperature


class Calorie:
    """
    BMR = 10 * weight + 6.25 * height - 5 * age + 5 + 0.05 * (temperature - 20)
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 + 0.05 * (self.temperature - 20)
        return BMR


Temp = Temperature("Russia", "Moscow")
calorie = Calorie(96, 175, 23, Temp.get_temperature())

print(calorie.temperature)
print(calorie.calculate())
