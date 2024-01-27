import requests
import re
from bs4 import BeautifulSoup


class Temperature:

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get_temperature(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        r = requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}", headers=headers)
        html_content = r.content
        soup = BeautifulSoup(html_content, "html5lib")
        # print(soup)
        element = soup.select_one("div[class='h2']")  # Find element
        if element is not None:
            text = element.text.strip()
            numeric_part = re.search(r'\d+', text).group()

            # Convert the numeric part to an integer
            numeric_value = int(numeric_part)
            return numeric_value
        else:
            print("Element not found.")




