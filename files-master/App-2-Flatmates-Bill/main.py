import time

from flat import Bill, Flatmate
from PDF_Report import PdfReport

new_bill = Bill(int(input("Hello there!!What is the monthly bill? ")), int(input("OK cool! What is the period of the "
                                                                                 "bill? ")))
flatmates = [input("What is your name? "), input("What is the name of other flatmate? ")]
days_stayed = [int(input("How many days "+flatmates[0]+" stayed? ")), int(input("How many days "+flatmates[1]+"stayed"
                                                                                                              "? "))]
Flatmate1 = Flatmate(flatmates[0], days_stayed[0], days_stayed)
Flatmate2 = Flatmate(flatmates[1], days_stayed[1], days_stayed)
print("Well, here we go !!!")
time.sleep(2)
print(flatmates[0]+" has to pay: " + str(Flatmate1.pays(new_bill)))
print(flatmates[1]+" has to pay: " + str(Flatmate2.pays(new_bill)))
print("Thank you for using our Bill app! Your PDF has been generated!")
pdf_report = PdfReport("Bill_Report.pdf")
pdf_report.generate(Flatmate1, Flatmate2, new_bill)
