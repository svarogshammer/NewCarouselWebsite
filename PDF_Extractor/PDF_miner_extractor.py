from lib2to3.fixer_util import p2

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO


class PDFMiner:

    def convert_pdf_to_text(self, filename):
        resource_manager = PDFResourceManager()
        resource_string = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(resource_manager, resource_string, laparams=laparams)

        try:
            fp = open(filename, 'rb')
        except FileNotFoundError:
            print("Could not open file")
            return ""
        else:
            interpreter = PDFPageInterpreter(resource_manager, device)
            password = ""
            max_pages = 0
            caching = True
            pagenos = set()

            for page in PDFPage.get_pages(fp, pagenos, maxpages=max_pages, password=password, caching=caching,
                                          check_extractable=True):
                interpreter.process_page(page)

            text = resource_string.getvalue()
            fp.close()
            device.close()
            resource_string.close()

            clean_text = self.clean_text(text)

            return clean_text

    def clean_text(self, text):
        clean_text = text.split('\n')
        return clean_text
