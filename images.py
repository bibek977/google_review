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

    def getImages():

        try:
            
            Driver.wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"photos")]/parent::button')))

            photos = Driver.driver.find_element(By.XPATH,'//div[contains(text(),"photos")]/parent::button')
            photos.click()
            time.sleep(5)

            element = Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label and @role="main"]/div[3]')))

            height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)
            while True:
                Driver.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', element)
                time.sleep(5)

                new_height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)

                if height == new_height:
                    break
                height = new_height

            image_list = []
            images = Driver.driver.find_elements(By.XPATH,'//a[@data-photo-index]/div[@role]')

            for i in images:
                image = i.get_attribute("style")
                img = image.split('url("')[1]
                new_img = img.split('")')[0]
                if new_img == "//:0":
                    new_img = "Not avialible"
                image_list.append(new_img)

            Driver.driver.back()

            # Title = Driver.driver.title


            image_list = [i for i in image_list if i != "Not avialible"]
            return image_list

            time.sleep(5)
            Driver.driver.quit()

        except Exception as e:

            print(e)



images = {

}

# data["Title"] = Driver.getImages()[0]
images["Company Images"] = Driver.getImages()

with open("images.json",'w') as f:
    json.dump(images,f)

Driver.driver.quit()