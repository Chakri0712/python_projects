class Bill:

    """
    Bill class contains bill amount and bill period
    """

    def __int__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    """
       Flatmate class contains name of the flatmate, no.of days he/she stayed in the house and
        method pays to know how much bill the flatmate needs to pay
       """

    def __int__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:

    """
       PdfReport class contains name of the pdf file and generate method which takes flatmates and bills
       as input to generate pdf
       """

    def __int__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


