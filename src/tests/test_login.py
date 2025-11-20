from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from ..pages import base_page

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
login_page = base_page.Page(driver=driver)

def main():
    login_page.open_page("https://parabank.parasoft.com/parabank/index.htm")
    assert "ParaBank" in driver.title

    log_in("username", "password")

    time.sleep(5)
    driver.close()

def log_in(username, password):
    username_field = login_page.get_element(name="username")
    username_field.send_keys(username)

    password_field = login_page.get_element(name="password")
    password_field.send_keys(password)

    login_button = login_page.get_element(text="Log In")
    login_button.click()

if __name__ == "__main__":
    main()