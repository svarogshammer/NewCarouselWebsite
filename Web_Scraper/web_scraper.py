import requests
import html5lib
from bs4 import BeautifulSoup
from re import search
import csv
import json


class WebScraper:
    results = []

    def get_urls(self, search_data):
        url = "https://www.google.com/search?q="
        url += search_data.get('unit-code') + search_data.get('questions')[0]
        url = url.replace(" ", "+")
        content = self.fetch(url)
        all_links = self.get_all_links(content)

        found_urls = ""

        print(" ")
        print("Assignment most likely found at")
        print(" ")
        for link in all_links:
            if "assignment" in link.get('url').lower():
                print("Url --- " + link.get('url'))
                found_urls += link.get('url') + " "

        return found_urls

    def get_matching_links(self, search_data, all_links):
        matching_links = []

        for link in all_links:
            match_count = 0
            extracted_words = []

    def fetch(self, url):
        print("HTTP GET request to URL: %s" % url, end='')
        res = requests.get(url)
        print(' | Status code: %s' % res.status_code)

        return res.text

    def get_all_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        links = []
        clean_links = []

        for temp in soup.find_all('div', class_="ZINbbc xpd O9g5cc uUPGi"):
            links.append(temp)

        for link in links:
            title = ""
            text = ""
            url = ""
            if link.find('div', class_="BNeawe vvjwJb AP7Wnd"):
                title = link.find('div', class_="BNeawe vvjwJb AP7Wnd").text

            if link.find('div', class_="BNeawe s3v9rd AP7Wnd"):
                text = link.find('div', class_="BNeawe s3v9rd AP7Wnd").text

            if link.find('a'):
                temp_url = link.find('a')['href']
                url_parts = temp_url.split("=")
                url_parts2 = url_parts[1].split("&")
                url = url_parts2[0]

            clean_link = {
                'title': title,
                'text': text,
                'url': url
            }
            clean_links.append(clean_link)

        return clean_links

