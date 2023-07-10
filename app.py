import pdfplumber
from datetime import date

# Read in the two example files
pdf1 = pdfplumber.open("example1.pdf")
pdf2 = pdfplumber.open("example2.pdf")


for page in pdf1.pages:
    text = page.extract_tables()
    print(text, '\n')

for page in pdf2.pages:
    text = page.extract_tables()
    print(text, '\n')
    
