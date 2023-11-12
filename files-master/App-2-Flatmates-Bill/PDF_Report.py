import webbrowser
import fpdf


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
                       "Monthly Bill for " + flatmate1.name + " for staying " + str(flatmate1.days_in_house) + " days: " + str(
                           flatmate1.pays(bill)))

        # Write the monthly bill for Anne to the PDF.
        pdf.multi_cell(100, 10,
                       "Monthly Bill for " + flatmate1.name + " for staying " + str(flatmate2.days_in_house) + " days: " + str(
                           flatmate2.pays(bill)))

        # Output the PDF.
        pdf.output(self.filename)

        # open pdf automatically
        webbrowser.open(self.filename)
