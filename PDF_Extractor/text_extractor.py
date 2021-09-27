from PDF_Extractor.PDF_miner_extractor import PDFMiner
from PDF_Extractor.pyPDF2_Extractor import PyPDF2Extractor


class TextExtractor:
    extractor = PDFMiner()
    extractor2 = PyPDF2Extractor()

    # Uses PDFMiner library to convert PDF, if it fails PyPDF2 is used instead, else no text is returned
    def convert_to_text(self, filename):
        text = ""
        text = self.extractor.convert_pdf_to_text(filename)

        if text == "":
            text = self.extractor2.convert_pdf_to_text(filename)

        return text

