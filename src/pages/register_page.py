from ..pages.base_page import Page

class RegisterPage(Page):
    def fill_fields(self, data):
        for name, val in data.items():
            input_elem = self.get_element(id=name)
            try:
                input_elem.clear()
            except Exception:
                pass
            input_elem.send_keys(val)
        confirm_field = self.get_element(id="repeatedPassword")
        confirm_field.send_keys(list(data.values())[-1])
        
        confirm_button = self.get_element(xpath="//input[contains(@value, 'Register')]")
        confirm_button.click()