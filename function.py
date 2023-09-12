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


class Driver:

    # options = Options()
    # options.headless = True
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)

    wait = WebDriverWait(driver,30)

def openPage():

    time.sleep(5)
    # assert "Nerd Platoon Pvt. Ltd. - Google Maps" in Driver.driver.title
    
    title = Driver.driver.title
    print(title)

    with open("title.txt","w") as f:
        f.write(f"Title : {title} \n")

def getImage():
      
    time.sleep(5)
    title = Driver.driver.title
    t = title.split(" -")[0]
    print(t)
    image_link = Driver.driver.find_element(By.XPATH,f"//button[@aria-label = 'Photo of {t}']").find_element(By.TAG_NAME,"img").get_attribute("src")
    print(image_link)


    with open("title.txt","a") as f:
        f.write(f"profile image : {image_link}\n  \n")

def getTitle():

    # time.sleep(5)
    # title = Driver.driver.find_element(By.XPATH,'//div[@role="region"]/div[1]/div[2]//h1')
    # print(title)

    stars = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"stars")]').get_attribute("aria-label")
    print(stars)

    with open("title.txt","a") as f:
        f.write(f"profile image : {stars}\n  \n")

    review = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"reviews")]').text
    print(review)

    with open("title.txt","a") as f:
        f.write(f"profile image : {review}\n  \n")

def getReviews():

    review_list = Driver.driver.find_elements(By.XPATH,"//div[@data-review-id]//div[@data-review-id]/div/div/button")
    for review in review_list:
        r = review.find_element(By.TAG_NAME,'img').get_attribute("src")
        print(r)

        with open("title.txt","a") as f:
            f.write(f"profile image  : {r}\n  \n")


    reviewer_name = Driver.driver.find_elements(By.XPATH,"//div[@data-review-id]//div[@data-review-id]/div/div[2]//button/div[1]")
    for i in reviewer_name:
        print(i.text)
        with open("title.txt","a") as f:
            f.write(f"name  : {i.text}\n  \n")

    # review_text = Driver.driver.find_elements(By.XPATH,"//div[@data-review-id]//div[@data-review-id]/div/div[4]/div[2]/div/span")
    review_text = Driver.driver.find_elements(By.XPATH,'//div[@class="MyEned"]/span')
    for j in review_text:
        print(j.text)   

        with open("title.txt","a") as f:
            f.write(f"description  : {j.text}\n  \n") 

def reviewNewest():

    time.sleep(10)
    # sort_button = Driver.wait.until(Ec.element_to_be_clickable((By.XPATH,"//button[@aria-label='Sort reviews']")))
    sort_button = Driver.driver.find_element(By.XPATH,"//button[@aria-label='Sort reviews']").click()
    # sort_button.click()

    time.sleep(5)

    new_review_button = Driver.driver.find_element(By.XPATH,"//div[@role='menu']/div[@role='menuitemradio'][2]")
    new_review_button.click()

    time.sleep(5)

    html = Driver.driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    time.sleep(5)
    # newest_review = Driver.driver.find_elements(By.XPATH,"//div[@aria-label and @data-review-id]")

    newest_review_image = Driver.driver.find_elements(By.XPATH,"//div[@aria-label and @data-review-id]/div/div/div/button/img")

    for r in newest_review_image:
        image_link = r.get_attribute("src")
        print(image_link)
        with open("title.txt","a") as f:
            f.write(f"profile image  : {image_link} \n \n")


    time.sleep(5)

    newest_review_name = Driver.driver.find_elements(By.XPATH,"//div[@aria-label and @data-review-id]/div/div/div[2]/div/div/button/div")

    for r in newest_review_name:
        name = r.text
        print(name)
        with open("title.txt","a") as f:
            f.write(f"name  : {name}\n  \n")

    time.sleep(5)
    
    newest_review_desc = Driver.driver.find_elements(By.XPATH,"//div[@aria-label and @data-review-id]/div/div/div[4]/div[2]/div/span")

    for r in newest_review_desc:
        d = r.text
        print(d)

        with open("title.txt","a") as f:
            f.write(f"description  : {d}\n  \n")

