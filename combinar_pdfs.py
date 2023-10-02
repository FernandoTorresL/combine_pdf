# Project: Combining select pages from many PDFs
#! python3
# combinar_pdfs.py - Combine all the PDFs in the current working directory
# into a single PDF
# Source: Book "Automate the Boring Stuff with Python", page 303
# Warning: You need to update some methods like PdfFileWriter to PdfWriter

# Step 1: Find all PDF files
import os

import PyPDF2

# Get all the PDF filenames
pdfFiles = []

path = os.path.join("./", "archivos_pdfs")

for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
# pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfWriter()

# Step 2: Open each PDF
# Loop through al the PDF files.
for filename in pdfFiles:
    filepath = os.path.join(path, filename)
    print(filename)
    pdfFileObj = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Step 3:Add each page
# Loop through all the pages (except the second) and add them
    for pageNum in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

# Step 4: Save the results
# Save the resulting PDF to a file.
pdfOutput = open('PDF_combinado.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
