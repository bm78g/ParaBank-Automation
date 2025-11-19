from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
    username_input = login_page.get_element(name="username")
    username_input.send_keys(username)

    password_input = login_page.get_element(name="password")
    password_input.send_keys(password)

    login_button = login_page.get_element(text="Log In")
    login_page.click(login_button)

if __name__ == "__main__":
    main()