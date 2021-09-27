import PyPDF2


class PyPDF2Extractor:

    def convert_pdf_to_text(self, pdf_file):
        my_pdf_file = PyPDF2.PdfFileReader(pdf_file)

        with open(pdf_file, 'w') as pdf_output:
            for page in range(my_pdf_file.getNumPages()):
                data = my_pdf_file.getPage(page).extractText()
                pdf_output.write(data.replace('. ', '\n'))
                pdf_output.close()

        with open(pdf_file, 'r') as myPDFContent:
            print(myPDFContent.read())
            myPDFContent.close()

