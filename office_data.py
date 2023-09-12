from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
from tags import *
import time

import json

class Driver:

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)

    wait = WebDriverWait(driver, 30)

    def getTitle():

        try:
            Title = Driver.driver.title

            return Title

        except Exception as e:
            print(e)

    def getName():

        try:

            Driver.wait.until(EC.presence_of_element_located((By.XPATH,"//h1/span/parent::h1")))
            name = Driver.driver.find_element(By.XPATH,"//h1/span/parent::h1").text

            return name

        except Exception as e:
            print(e)
        
    def getRating():

        try:
            Driver.wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@aria-label,"stars") and @role="img"][1]')))
            stars = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"stars") and @role="img"][1]').get_attribute('aria-label')

            Driver.wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@aria-label,"reviews")]')))
            total = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"reviews")]').get_attribute('aria-label')

            return {
                "stars" : stars,
                "total" : total
            }
        
        except Exception as e:
            print(e)

    def getOfficeData():

        try:
            Driver.wait.until(EC.presence_of_all_elements_located(((By.XPATH,'//div[contains(@aria-label,"Information for")]//button/div/div[2]/div[1]'))))
            data = Driver.driver.find_elements(By.XPATH,'//div[contains(@aria-label,"Information for")]//button/div/div[2]/div[1]')

            info_list = []
            for i in data:
                info = i.text
                info_list.append(info)

            return info_list

        except Exception as e:
            print(e)

Driver.getTitle()
Driver.getName()
Driver.getRating()
Driver.getOfficeData()

Driver.driver.quit()