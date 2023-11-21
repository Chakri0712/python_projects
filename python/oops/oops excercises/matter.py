class Matter:
    
    # class variables
    boiling_temperature = None
    freezing_temperature = None

    # here temperature is instance variable
    def __init__(self, temperature):
        self.temperature = temperature

    def state(self):
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        elif self.freezing_temperature < self.temperature < self.boiling_temperature:
            return 'liquid'
        else:
            return 'gas'
            
class Water(Matter):
    boiling_temperature = 100
    freezing_temperature = 0
        
class Mercury(Matter):
    boiling_temperature = 356.7
    freezing_temperature = -38.83

water = Water(50)
print(water.state())

mercury = Mercury(100.15)
print(mercury.state())