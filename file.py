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

    def reviewRelevant():

        try:
            
            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Reviews for")]')))
            button = Driver.driver.find_element(By.XPATH, '//button[contains(@aria-label,"Reviews for")]')
            button.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')))
            sort = Driver.driver.find_element(By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')
            sort.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="menu"]/div[@data-index][1]')))
            relevant = Driver.driver.find_element(By.XPATH, '//div[@role="menu"]/div[@data-index][1]')
            relevant.click()


            element = Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label and @role="main"]/div[2]')))

            height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)
            while True:
                Driver.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', element)
                time.sleep(5)

                new_height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)

                if height == new_height:
                    break
                height = new_height


            reviews = Driver.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@aria-label and @data-review-id]')))
            
            review = {}
            for i in reviews:

                image = i.find_element(By.XPATH,'div/div/div/button/img').get_attribute('src')
                name = i.find_element(By.XPATH,'div/div/div[2]/div[2]/div/button/div[1]').text

                try:
                    desc = i.find_element(By.XPATH,'div/div/div[4]/div[2]/div/span[1]').text
                except NoSuchElementException:
                    desc = "Not rated"

                stars = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[1]').get_attribute('aria-label')
                date = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[2]').text

                # print(f"{name}\n {image}\n \n{desc}\n \n{date}")
                review[name] = {"Image" :  image, "Rate" : stars, "Time" : date, "Body" :  desc}
            return review

        except Exception as e:
            print(e)
            Driver.driver.quit()
    
    def reviewNewest():

        try:
            
            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Reviews for")]')))
            button = Driver.driver.find_element(By.XPATH, '//button[contains(@aria-label,"Reviews for")]')
            button.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')))
            sort = Driver.driver.find_element(By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')
            sort.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="menu"]/div[@data-index][2]')))
            relevant = Driver.driver.find_element(By.XPATH, '//div[@role="menu"]/div[@data-index][2]')
            relevant.click()


            element = Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label and @role="main"]/div[2]')))

            height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)
            while True:
                Driver.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', element)
                time.sleep(5)

                new_height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)

                if height == new_height:
                    break
                height = new_height


            reviews = Driver.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@aria-label and @data-review-id]')))
            
            review = {}
            for i in reviews:

                image = i.find_element(By.XPATH,'div/div/div/button/img').get_attribute('src')
                name = i.find_element(By.XPATH,'div/div/div[2]/div[2]/div/button/div[1]').text

                try:
                    desc = i.find_element(By.XPATH,'div/div/div[4]/div[2]/div/span[1]').text
                except NoSuchElementException:
                    desc = "Not rated"

                stars = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[1]').get_attribute('aria-label')
                date = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[2]').text

                # print(f"{name}\n {image}\n \n{desc}\n \n{date}")
                review[name] = {"Image" :  image, "Rate" : stars, "Time" : date, "Body" :  desc}
            return review

        except Exception as e:
            print(e)
            Driver.driver.quit()
    
    
    def reviewHighest():

        try:
            
            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Reviews for")]')))
            button = Driver.driver.find_element(By.XPATH, '//button[contains(@aria-label,"Reviews for")]')
            button.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')))
            sort = Driver.driver.find_element(By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')
            sort.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="menu"]/div[@data-index][3]')))
            relevant = Driver.driver.find_element(By.XPATH, '//div[@role="menu"]/div[@data-index][3]')
            relevant.click()


            element = Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label and @role="main"]/div[2]')))

            height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)
            while True:
                Driver.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', element)
                time.sleep(5)

                new_height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)

                if height == new_height:
                    break
                height = new_height


            reviews = Driver.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@aria-label and @data-review-id]')))
            
            review = {}
            for i in reviews:

                image = i.find_element(By.XPATH,'div/div/div/button/img').get_attribute('src')
                name = i.find_element(By.XPATH,'div/div/div[2]/div[2]/div/button/div[1]').text

                try:
                    desc = i.find_element(By.XPATH,'div/div/div[4]/div[2]/div/span[1]').text
                except NoSuchElementException:
                    desc = "Not rated"

                stars = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[1]').get_attribute('aria-label')
                date = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[2]').text

                # print(f"{name}\n {image}\n \n{desc}\n \n{date}")
                review[name] = {"Image" :  image, "Rate" : stars, "Time" : date, "Body" :  desc}
            return review

        except Exception as e:
            print(e)
            Driver.driver.quit()

    def reviewLowest():

        try:
            
            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Reviews for")]')))
            button = Driver.driver.find_element(By.XPATH, '//button[contains(@aria-label,"Reviews for")]')
            button.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')))
            sort = Driver.driver.find_element(By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')
            sort.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="menu"]/div[@data-index][4]')))
            relevant = Driver.driver.find_element(By.XPATH, '//div[@role="menu"]/div[@data-index][4]')
            relevant.click()


            element = Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label and @role="main"]/div[2]')))

            height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)
            while True:
                Driver.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', element)
                time.sleep(5)

                new_height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)

                if height == new_height:
                    break
                height = new_height


            reviews = Driver.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@aria-label and @data-review-id]')))
            
            review = {}
            for i in reviews:

                image = i.find_element(By.XPATH,'div/div/div/button/img').get_attribute('src')
                name = i.find_element(By.XPATH,'div/div/div[2]/div[2]/div/button/div[1]').text

                try:
                    desc = i.find_element(By.XPATH,'div/div/div[4]/div[2]/div/span[1]').text
                except NoSuchElementException:
                    desc = "Not rated"

                stars = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[1]').get_attribute('aria-label')
                date = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[2]').text

                # print(f"{name}\n {image}\n \n{desc}\n \n{date}")
                review[name] = {"Image" :  image, "Rate" : stars, "Time" : date, "Body" :  desc}
            return review

        except Exception as e:
            print(e)
            Driver.driver.quit()


data = {

}

data["Relevant Review List"] = Driver.reviewNewest()
data["Newest Review List"] = Driver.reviewNewest()
data["Highest Review List"] = Driver.reviewHighest()
data["Lowest Review List"] = Driver.reviewLowest()

with open("google.json",'w') as f:
    json.dump(data,f)

Driver.driver.quit()

