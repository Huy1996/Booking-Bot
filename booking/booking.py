import os
import booking.constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r'C:\Selenium-Driver', teardown=False):
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)     # Detach the browser after program done
        chr_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chr_options.add_argument("--headless=chrome")              # Enter headless mode with no GUI
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__(options=chr_options)
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency="USD"):
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[class="fc63351294 a822bdf511 e3c025e003 cfb238afa1 c334e6f658 e634344169"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.XPATH,
            f'//div[text()="{currency}"]'
        )
        selected_currency_element.click()

    def close_login_modal(self):
        try:
            login_modal = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Dismiss sign-in info."]'
            )
            login_modal.click()
        except:
            pass

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ":Ra9:")
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR,
            'ul[class="ce50aa40cd d319063cd8 b530332a61"] > li:nth-child(1)'    
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        self._select_date(check_in_date)

        month_check_in = int(check_in_date[5:7])
        month_check_out = int(check_out_date[5:7])
        if (count:=(month_check_out - month_check_in)) > 1:
            next_month_button = self.find_element(
                By.CSS_SELECTOR,
                'button[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 cfb238afa1 c334e6f658 ae1678b153 c9fa5fc96d be298b15fa"]'
            )
            for i in range(count - 1):
                next_month_button.click()

        self._select_date(check_out_date)

    def _select_date(self, date):
        date_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{date}"]'
        )
        date_element.click()

    def select_room_capacity(self, adult=2, children=0, room=1, age_list=None):
        room_element = self.find_element(
            By.CSS_SELECTOR,
            'button[class="d47738b911 b7d08821c3"]'
        )
        room_element.click()

        self._select_num("group_adults", adult)
        self._select_num("group_children", children)
        # TODO: Need to implement function to choose age of children
        self._select_num("no_rooms", room)

        

        done_button = self.find_element(
            By.CSS_SELECTOR,
            'button[class="fc63351294 a822bdf511 e2b4ffd73d f7db01295e c938084447 a9a04704ee d285d0ebe9"]'
        )
        done_button.click()

    

    def _select_num(self, _id, num):
        element = self.find_element(
            By.ID,
            f"{_id}"
        )
        left_btn = element.find_element(
            By.XPATH,
            'following-sibling::div[2]/button[1]'
        )
        default_val = left_btn.find_element(
            By.XPATH,
            'following-sibling::span'
        ).text
        right_btn = element.find_element(
            By.XPATH,
            'following-sibling::div[2]/button[2]'
        )
        while (count:=(num - int(default_val))) != 0:
            if count < 0:
                left_btn.click()
                num += 1
            else:
                right_btn.click()
                num -= 1

    def click_search(self):
        search_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_btn.click()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(2,5)
        self.refresh()
        filtration.sort_price_lowest_first()
   
    def report_results(self):
        hotel_boxes = self.find_element(
            By.ID, 
            "search_results_table"
        )
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Link", "Hotel Price"],
        )
        table.add_rows(report.pull_titles())
        print(table)
    