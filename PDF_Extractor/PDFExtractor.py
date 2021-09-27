from PDF_Extractor.text_extractor import TextExtractor
from PDF_Extractor.keyword_extractor import KeywordExtractor


class PDFExtractor:
    text_extractor = TextExtractor()
    keywordExtractor = KeywordExtractor()

    def extract_search_data(self, filename):
        self.keywordExtractor.text = self.text_extractor.convert_to_text(filename)
        search_data = self.keywordExtractor.get_search_data()

        return search_data


