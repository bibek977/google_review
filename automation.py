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

import json


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
            Title = Driver.driver.title

            photos = Driver.driver.find_element(By.XPATH,'//div[contains(text(),"photos")]/parent::button')
            photos.click()

            time.sleep(5)

            image_list = []
            images = Driver.driver.find_elements(By.XPATH,'//a[@data-photo-index]/div[@role]')
            for i in images:
                image = i.get_attribute("style")
                print(image)
                image_list.append(image)

            Driver.driver.back()

            # return {
            #     "Title" : Title,
            #     "Images" : image_list
            # }
            return Title, image_list

        except Exception as e:
            print(e)

    def getName():

        try:
            time.sleep(5)
            name = Driver.driver.find_element(By.XPATH,"//h1/span/parent::h1").text
            print(name)

            # return {
            #     'name' : name
            # }

            return name

        except Exception as e:
            print(e)

    def getRating():

        try:
            time.sleep(5)
            stars = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"stars") and @role="img"][1]').get_attribute('aria-label')
            print(stars)

            total = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"reviews")]').get_attribute('aria-label')
            print(total)

            return stars,total
        
        except Exception as e:
            print(e)

    def getOfficeData():

        try:
            time.sleep(5)
            data = Driver.driver.find_elements(By.XPATH,'//div[contains(@aria-label,"Information for")]//button/div/div[2]/div[1]')

            info_list = []
            for i in data:
                info = i.text
                print(info)
                info_list.append(info)

            return info_list

        except Exception as e:
            print(e)

    def getReviews():

        try:
            time.sleep(5)
            button = Driver.driver.find_element(By.XPATH,'//button[contains(@aria-label,"Reviews for")]')
            button.click()
            time.sleep(10)

            sort = Driver.driver.find_element(By.XPATH,'//span[contains(text(),"Sort")]//ancestor::button')
            sort.click()
            time.sleep(5)

            relevant = Driver.driver.find_element(By.XPATH,'//div[@role="menu"]/div[@data-index][2]')
            relevant.click()
            time.sleep(5)

            reviews = Driver.driver.find_elements(By.XPATH,'//div[@aria-label and @data-review-id]')

            r_image = []
            r_name = []
            r_stars = []
            r_date = []

            review = {}
            for i in reviews:

                image = i.find_element(By.XPATH,'div/div/div/button/img').get_attribute('src')
                name = i.find_element(By.XPATH,'div/div/div[2]/div[2]/div/button/div[1]').text
                # desc = i.find_element(By.XPATH,'div/div/div[4]/div[2]/div/span[1]').text
                stars = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[1]').get_attribute('aria-label')
                date = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[2]').text
                print(f'{name} : {image} \n {stars} : {date} \n \n ')

                r_image.append(image)
                r_name.append(name)
                r_stars.append(stars)
                r_date.append(date)

                review[name] = [image,stars,date]

            # return r_date,r_name,r_image,r_stars
            return review

        except Exception as e:
            print(e)

    def quit():
        
        time.sleep(5)
        Driver.driver.quit()

# Driver.getImages()
# Driver.getName()
# Driver.getRating()
# Driver.getOfficeData()
# Driver.getReviews()
# Driver.quit()

data = {

}

data['title'] = Driver.getImages()[0]
data['company images'] = Driver.getImages()[1]
data['Company name'] = Driver.getName()
data['Company Rating'] = Driver.getRating()[0]
data['Total Review user'] = Driver.getRating()[1]
data['Company Details'] = Driver.getOfficeData()
data['Review List'] = Driver.getReviews()

print(data)

with open("new.json",'w') as f:
    json.dump(data,f)