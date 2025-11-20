from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from ..pages.login_page import LoginPage

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
login_page = LoginPage(driver=driver)

def main():
    login_page.open_page("https://parabank.parasoft.com/parabank/index.htm")
    assert "ParaBank" in driver.title

    login_page.login("username", "password")

    time.sleep(3)
    driver.close()

if __name__ == "__main__":
    main()