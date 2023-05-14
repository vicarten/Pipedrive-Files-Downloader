# import all packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

#information(inputs)
login = input("Enter your Pipedrive Login: ")
password = input("Enter your Pipedrive Password: ")
url = input("Enter the URL of the page from which you want to download the files: ")

while url != "0":
    # open a new window
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    # login to Pipedrive
    driver.find_element("name", "login").send_keys(login)
    driver.find_element("name", "password").send_keys(password + "\n")

    # click to all 'show all' buttons
    time.sleep(5)

    def show_all():
        try:
            wait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Show all']"))).click()
            show_all()
        except TimeoutException:
            pass

    time.sleep(1)
    show_all()

    # click to all 'more actions' buttons
    dropdowns = driver.find_elements(By.XPATH, "//button[@aria-label='More actions']//*[name()='svg']")

    for i in range(1, len(dropdowns) + 1):
        wait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, f"(//button[@aria-label='More actions']//*[name()='svg'])[{str(i)}]"))).click()

        try:
            driver.find_element(By.XPATH, "//span[normalize-space()='Download']")
            wait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Download']"))).click()
        except NoSuchElementException:
            pass

        wait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, f"(//button[@aria-label='More actions']//*[name()='svg'])[{str(i)}]"))).click()

    driver.quit()

    url = input("Enter the URL of the page from which you want to download the files or enter 0 to exit: ")




