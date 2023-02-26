from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

from bot import text

import requests

URL = "https://avidreaders.ru/"


class Parse():
    def parser(self, url):
        r = requests.get(URL)
        soup = bs(r.text, "lxml")
        self.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/span").click()
        self.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[4]/input").send_keys(book)

