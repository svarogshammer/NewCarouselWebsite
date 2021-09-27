import re


class KeywordExtractor:
    text = ""

    def get_search_data(self):
        query_data = {
            'unit-code': self.find_unit_code(),
            'questions': self.find_questions(),
            'keywords': self.find_keywords()
        }

        return query_data

    def find_unit_code(self):
        pattern = re.compile('.*[a-zA-Z]{3}[0-9]{5}.*')

        for i in self.text:
            match_string = i
            result = re.match(pattern, match_string)
            if result:
                return match_string

    def find_questions(self):
        questions = []
        # one capital, all non symbols followed by one symbol
        # questionPattern = re.compile(r'(([A-Z|[0-9]+\.)[^\.!?]*[\?])')
        question_pattern = re.compile(r'(([A-Z|[0-9]+\.)[^\.!?]*[\?|\.])')

        for i in self.text:
            match_string = i
            result = re.match(question_pattern, match_string)
            if result:
                questions.append(match_string)

        return questions

    def find_keywords(self):
        keywords = ""
        keywords += "Chegg, Assignment"

        return keywords



