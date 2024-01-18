import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json


class TrainParse():
    def __init__(self, parse_info_path) -> None:
        assert os.path.exists(parse_info_path), "The file upload_information.json is not exist."
        with open(parse_info_path, 'r') as file:
            parse_info = json.load(file)
        self.parse_info = parse_info["train_config"]
        # Initial the driver 
        self._init_chromedriver()
        self.tap_number = 0
    
    def _init_chromedriver(self) -> None:
        """ Update WebDriver """
        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def wait_for_element(self, by=None, label=None, timeout=10) -> WebDriverWait:
        """ locate element until hit 10sec limit """
        assert by , "Missing part: BY."
        assert label , "Missing part: label."
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, label)))
    
    def enter_text(self, by, label, text) -> None:
        """ Input txt to the target element """
        element = self.wait_for_element(by, label)
        element.send_keys(text)

    def click_element(self, by, label) -> None:
        """ Click the target element """
        button = self.wait_for_element(by, label)
        button.click()

    def close_driver(self) -> None:
        self.driver.quit()

    def open_train_hpmepage(self) -> None:
        try:
            self.driver.get(self.parse_info['URL'])
        except Exception as e:
            print(f"Login Error: {e}")

    def switch_to_shuttle(self) -> None:
        self.click_element(by=By.XPATH, label="/html/body/div[5]/div[3]/form/div[2]/div[4]/select")
        self.click_element(by=By.XPATH, label="/html/body/div[5]/div[3]/form/div[2]/div[4]/select/option[8]")
    
    def confirm_search(self) -> None:
        self.click_element(by=By.XPATH, label="/html/body/div[5]/div[3]/form/div[3]/button")

    def find_price(self) -> None:
        price_element = self.driver.find_element(By.CSS_SELECTOR, '.rightnote.price .red')
        return price_element.text
