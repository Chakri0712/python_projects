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

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return ((bill.amount / 30) / 2) * self.days_in_house


class PdfReport:
    """
       PdfReport class contains name of the pdf file and generate method which takes flatmates and bills
       as input to generate pdf
       """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


new_bill = Bill(int(input("What is the monthly bill? ")), "Monthly")
Jack = Flatmate("Jack", int(input("How many days Jack stayed? ")))
Anne = Flatmate("Anne", int(input("How many days Anne stayed? ")))
print("Jack has to pay: " + str(Jack.pays(new_bill)))
print("Anne has to pay: " + str(Anne.pays(new_bill)))
