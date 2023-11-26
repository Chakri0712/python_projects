# Importing custom modules
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

# importing classes
from flatmates_bill.PDF_Report import PdfReport
from flatmates_bill.flat import Bill, Flatmate

app = Flask(__name__)


# Class for handling the home page
class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


# Class for handling the Bill Form page
class BillFormPage(MethodView):
    def get(self):
        # Create an instance of the BillForm class
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        # Create an instance of the BillForm class and populate it with data from the request
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = float(bill_form.period.data)

        # Create a Bill object
        the_bill = Bill(amount, period)

        # Extract data for flatmate 1
        name_1 = bill_form.name1.data
        days_1 = int(bill_form.days_in_house1.data)

        # Extract data for flatmate 2
        name_2 = bill_form.name2.data
        days_2 = int(bill_form.days_in_house2.data)

        days = [days_1, days_2]

        # Create Flatmate objects
        flatmate1 = Flatmate(name_1, days_1, days)
        flatmate2 = Flatmate(name_2, days_2, days)

        # Calculate the amount each flatmate needs to pay
        amount1 = flatmate1.pays(the_bill)
        amount2 = flatmate2.pays(the_bill)

        # Create a PdfReport object and generate the PDF report
        pdf_report = PdfReport("Report.pdf")
        pdf_report.generate(flatmate1, flatmate2, the_bill)

        # Render the result on the bill form page
        return render_template('bill_form_page.html', name_1=name_1, amount1=amount1, name_2=name_2, amount2=amount2,
                               billform=bill_form, result=True)


"""First we have created a separate class for viewing result but later as as improvement we are showing the result in 
the bill form page itself so commented out the ResultPage"""


# class ResultPage(MethodView):
#
#     def post(self):
#         same code from post method of BillFormPage class

# Form class representing the bill form
class BillForm(Form):
    amount = StringField("Bill Amount: ", default='100')
    period = StringField("Bill Period: ", default='30')
    name1 = StringField("Name1: ", default='Prabha')
    days_in_house1 = StringField("days_in_house: ", default='20')
    name2 = StringField("Name2: ", default='Gobi')
    days_in_house2 = StringField("days_in_house: ", default='20')
    submit = SubmitField("Calculate")


# Add URL rules for the views
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultPage.as_view('result_page'))

# Start the Flask application
app.run()
