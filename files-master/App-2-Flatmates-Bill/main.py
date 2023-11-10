import fpdf


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
        return (bill.amount / sum(days_stayed)) * self.days_in_house


class PdfReport:
    """
       PdfReport class contains name of the pdf file and generate method which takes flatmates and bills
       as input to generate pdf
       """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = fpdf.FPDF()
        pdf.add_page()

        # Set the font for the heading.
        pdf.set_font("Arial", "B", 16)

        # Write the heading to the PDF.
        pdf.multi_cell(100, 10, "Total Monthly Bill: " + str(bill.amount))

        # Set the font for the body text.
        pdf.set_font("Arial", "", 12)

        # Write the monthly bill for Jack to the PDF.
        pdf.multi_cell(100, 10, "Monthly Bill for Jack: " + str(flatmate1.pays(new_bill)))

        # Write the monthly bill for Anne to the PDF.
        pdf.multi_cell(100, 10, "Monthly Bill for Anne: " + str(flatmate2.pays(new_bill)))

        # Output the PDF.
        pdf.output(self.filename)


new_bill = Bill(int(input("What is the monthly bill? ")), "Monthly")
days_stayed = [int(input("How many days Jack stayed? ")), int(input("How many days Anne stayed? "))]
Jack = Flatmate("Jack", days_stayed[0])
Anne = Flatmate("Anne", days_stayed[1])
print("Jack has to pay: " + str(Jack.pays(new_bill)))
print("Anne has to pay: " + str(Anne.pays(new_bill)))
pdf_report = PdfReport("Bill_Report.pdf")
pdf_report.generate(Jack, Anne, new_bill)
