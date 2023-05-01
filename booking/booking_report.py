# This file is going to include method that will parse
# the specific data that we need from each one of the deal boxes.

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

import pyshorteners

def shorten_link(full_link):
    shortener = pyshorteners.Shortener()
    link = shortener.tinyurl.short(full_link)
    return link

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR,
            'div[class="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"]'
        )
    
    def pull_titles(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR,
                'div[class="fcab3ed991 a23c043802"]'
            ).get_attribute('innerHTML').strip()

            hotel_url =  deal_box.find_element(
                By.CSS_SELECTOR,
                'a[class="e13098a59f"]'
            ).get_attribute('href').strip()
            
            link = shorten_link(hotel_url)

            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR,
                'span[class="fcab3ed991 fbd1d3018c e729ed5ab6"]'
            ).get_attribute('innerHTML').strip()
            collection.append((hotel_name, link, hotel_price))
        return collection
