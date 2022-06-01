from selenium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

path = r'chromedriver'
url = "https://www.youtube.com/"
   

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Vivek Kumar/AppData/Local/Google/Chrome/User Data/")

driver = webdriver.Chrome(executable_path="chromedriver",options=options)
driver.maximize_window()
driver.get(url)

wait = ui.WebDriverWait(driver,300)
while True:
    try:
        if EC.presence_of_element_located((By.XPATH,".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")):
            button=driver.find_element_by_xpath(".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
            driver.execute_script("arguments[0].click();",button)
            print("Skipped")
            sleep(2)
        else:
             continue
    except NoSuchElementException:
        print("skip button not found")
        sleep(2)

