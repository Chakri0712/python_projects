class Bill:
    """
    Bill class contains bill amount and bill period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
       Flatmate class contains name of the flatmate, no.of days he/she stayed in the house and
        method pays to know how much bill the flatmate needs to pay
       """

    def __init__(self, name, days_in_house, days_stayed):
        self.name = name
        self.days_in_house = days_in_house
        self.days_stayed = days_stayed

    def pays(self, bill):
        return round((bill.amount / sum(self.days_stayed)) * self.days_in_house,2)
