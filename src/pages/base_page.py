# Superclass of other page objects with basic functionalities for accessing the page and its elements.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def get_element(self, *, id=None, class_name=None, name=None, xpath=None, text=None):
        locator = None
        if id is not None:
            locator = (By.ID, id)
        elif class_name is not None:
            locator = (By.CLASS_NAME, class_name)
        elif name is not None:
            locator = (By.NAME, name)
        elif xpath is not None:
            locator = (By.XPATH, xpath)
        elif text is not None:
            xpath = (
                f"//button[normalize-space(.)=\"{text}\"] | "
                f"//a[normalize-space(.)=\"{text}\"] | "
                f"//input[@value=\"{text}\"]"
            )
            locator = (By.XPATH, xpath)
        else:
            raise ValueError("get_element ran without sufficient parameters.")

        return self.wait.until(EC.presence_of_element_located(locator))
    
    def get_text(self, element):
        if isinstance(element, tuple):
            elem = self.wait.until(EC.presence_of_element_located(element))
        else:
            elem = element
        return elem.text
    
    def open_page(self, url):
        self.driver.get(url)