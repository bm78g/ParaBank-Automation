from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from ..pages.register_page import RegisterPage

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
page = RegisterPage(driver=driver)

def main():
    page.open_page("https://parabank.parasoft.com/parabank/index.htm")
    assert "ParaBank" in driver.title

    register_link = page.get_element(xpath="//a[contains(@href,'register')]")
    register_link.click()

    data = {
        "customer.firstName" : "Robert",
        "customer.lastName" : "Robertson",
        "customer.address.street" : "1234 Elm Street",
        "customer.address.city" : "Gotham",
        "customer.address.state" : "Pennsylvania",
        "customer.address.zipCode" : "12345",
        "customer.phoneNumber" : "123-456-7890",
        "customer.ssn" : "123-45-6789",
        "customer.username" : "thebestqaengineer",
        "customer.password" : "password"
    }

    page.fill_fields(data)

    time.sleep(1)
    driver.close()

if __name__ == "__main__":
    main()