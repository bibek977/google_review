from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from tags import *
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import json
from selenium.webdriver.common.action_chains import ActionChains
from tags import url
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class Driver:

    # options = Options()
    # options.headless = True
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)
    wait = WebDriverWait(driver,30)


    def getImages():

            try:
                time.sleep(5)
                photos = Driver.driver.find_element(By.XPATH,'//div[contains(text(),"photos")]/parent::button')
                photos.click()

                time.sleep(5)

                image_list = []
                images = Driver.driver.find_elements(By.XPATH,'//a[@data-photo-index]/div[@role]')
                for i in images:
                    image = i.get_attribute("style")
                    # ActionChains(Driver.driver)\
                    # .scroll_to_element(i)\
                    # .perform()
                    Driver.driver.send_keys(Keys.PAGE_DOWN)
                    print(image)
                    image_list.append(image)

                Driver.driver.back()

            except Exception as e:
                print(e)


Driver.getImages()