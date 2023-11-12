import time
import webbrowser
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
        return round((bill.amount / sum(days_stayed)) * self.days_in_house)


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

        # adding image as an icon by giving path and dimensions
        image_path = "files/house.png"
        pdf.image(image_path, 10, 10, 20, 20)

        # giving space in terms of height
        pdf.ln(20)

        # setting x-position for the header
        pdf.set_x(50)

        # Set the font for the heading.
        pdf.set_font("Arial", "BU", 16)

        # Write the heading to the PDF.
        pdf.multi_cell(100, 10, "Monthly Bill")

        # Set the font for the body text.
        pdf.set_font("Arial", "", 12)

        # setting margins for body
        pdf.set_margins(50, 0, 50)

        pdf.set_x(50)

        pdf.multi_cell(100, 10, "Total Monthly Bill: " + str(bill.amount))

        pdf.multi_cell(100, 10, "Period(in days): " + str(bill.period))

        # Write the monthly bill for Jack to the PDF.
        pdf.multi_cell(100, 10,
                       "Monthly Bill for " + Flatmate1.name + " for staying " + str(flatmate1.days_in_house) + " days: " + str(
                           flatmate1.pays(new_bill)))

        # Write the monthly bill for Anne to the PDF.
        pdf.multi_cell(100, 10,
                       "Monthly Bill for " + Flatmate2.name + " for staying " + str(flatmate2.days_in_house) + " days: " + str(
                           flatmate2.pays(new_bill)))

        # Output the PDF.
        pdf.output(self.filename)

        # open pdf automatically
        webbrowser.open(self.filename)


new_bill = Bill(int(input("Hello there!!What is the monthly bill? ")), int(input("OK cool! What is the period of the "
                                                                                 "bill?")))
days_stayed = [int(input("How many days Jack stayed? ")), int(input("How many days Anne stayed? "))]
Flatmate1 = Flatmate("Jack", days_stayed[0])
Flatmate2 = Flatmate("Anne", days_stayed[1])
print("Well, here we go !!!")
time.sleep(2)
print("Jack has to pay: " + str(Flatmate1.pays(new_bill)))
print("Anne has to pay: " + str(Flatmate2.pays(new_bill)))
print("Thank you for using our Bill app! Your PDF has been generated!")
pdf_report = PdfReport("Bill_Report.pdf")
pdf_report.generate(Flatmate1, Flatmate2, new_bill)
