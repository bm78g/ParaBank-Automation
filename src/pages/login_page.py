from ..pages.base_page import Page

class LoginPage(Page):
    def login(self, username, password):
        username_field = self.get_element(name="username")
        username_field.send_keys(username)

        password_field = self.get_element(name="password")
        password_field.send_keys(password)

        login_button = self.get_element(text="Log In")
        login_button.click()