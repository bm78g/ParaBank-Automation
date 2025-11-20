from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from ..pages import base_page

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
register_page = base_page.Page(driver=driver)

def main():
    register_page.open_page("https://parabank.parasoft.com/parabank/index.htm")
    assert "ParaBank" in driver.title

    register_link = register_page.get_element(xpath="//a[contains(@href,'register')]")
    register_link.click()

    register("fname", "lname", "address", "city", "california", "11111", "1234567890", 
             "123456789", "username", "password")

    time.sleep(3)
    driver.close()

def register(fname, lname, addr, city, state, zip, phone, ssn, username, password):
    fname_field = register_page.get_element(id="customer.firstName")
    fname_field.send_keys(fname)

    lname_field = register_page.get_element(id="customer.lastName")
    lname_field.send_keys(lname)

    addr_field = register_page.get_element(id="customer.address.street")
    addr_field.send_keys(addr)

    city_field = register_page.get_element(id="customer.address.city")
    city_field.send_keys(city)

    state_field = register_page.get_element(id="customer.address.state")
    state_field.send_keys(state)

    zip_field = register_page.get_element(id="customer.address.zipCode")
    zip_field.send_keys(zip)

    phone_field = register_page.get_element(id="customer.phoneNumber")
    phone_field.send_keys(phone)

    ssn_field = register_page.get_element(id="customer.ssn")
    ssn_field.send_keys(ssn)

    username_field = register_page.get_element(id="customer.username")
    username_field.send_keys(username)

    password_field = register_page.get_element(id="customer.password")
    password_field.send_keys(password)

    confirm_field = register_page.get_element(id="repeatedPassword")
    confirm_field.send_keys(password)

    register_button = register_page.get_element(xpath="//input[contains(@type, 'submit')]")
    register_button.click()

if __name__ == "__main__":
    main()