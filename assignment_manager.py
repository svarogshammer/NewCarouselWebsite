from PDF_Extractor.PDFExtractor import PDFExtractor
from Web_Scraper.web_scraper import WebScraper
import mysql.connector


class AssignmentManager:
    pdf_extractor = PDFExtractor()
    web_scraper = WebScraper()

    def test(self, filename):
        search_data = self.pdf_extractor.extract_search_data(filename)

        id = 76
        keywords = search_data.get('unit-code') + search_data.get('questions')[0]
        title = "Assignment1b"
        coursecode = "COS30019"
        url = self.web_scraper.get_urls(search_data)

        # DeanDatabase: database-1.c18goo9xcwlq.us-east-1.rds.amazonaws.com
        db = mysql.connector.connect(host='database-1.c18goo9xcwlq.us-east-1.rds.amazonaws.com', user='admin',
                                    password='12349876', db="database-1")
        #db = mysql.connector.connect(host='instance1.cyrozt6t970f.us-east-1.rds.amazonaws.com', user='admin',
        #                            password='12349876', db="assignments")
        
        cursor = db.cursor()

        sql_query = """INSERT INTO scrapeddata (id, coursecode, title, keywords, url) VALUES (%s, %s, %s, %s, %s)"""
        tuple1 = (id, coursecode, title, keywords, url)
        cursor.execute(sql_query, tuple1)

        #sql_query = """INSERT INTO scrapeddata (AssignmentID, UnitCode, Name, Keywords, URLs) VALUES (%s, %s, %s, %s, %s)"""
        #tuple1 = (AssignmentID, UnitCode, Name, Keywords, URLs)
        #cursor.execute(sql_query, tuple1)
        # cursor.execute("DELETE from Assignments")

        db.commit()

        return search_data
