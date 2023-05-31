from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
#import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class TestSearcLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    # LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """li:nth-child(2) > a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")
    


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSearcLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearcLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestSearcLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearcLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        self.find_element(TestSearcLocators.LOCATOR_LOGIN_BTN).click()

    # def get_error_text(self):
    #     error_field = self.find_element(TestSearcLocators.LOCATOR_ERROR_FIELD, time=2)
    #     text = error_field.text
    #     logging.info(f"We find text {text} in error field {TestSearcLocators.LOCATOR_ERROR_FIELD[1]}")
    #     return text
    
    def click_contact_button(self):
        self.find_element(TestSearcLocators.LOCATOR_CONTACT_BTN).click()

    def enter_name(self, word):
        logging.info(f"Send '{word}' to element {TestSearcLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearcLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send '{word}' to element {TestSearcLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearcLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send '{word}' to element {TestSearcLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearcLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_contact_us_button(self):
        # time.sleep(1)
        logging.info('Click button "Contact us"')
        self.find_element(TestSearcLocators.LOCATOR_CONTACT_US_BTN).click()

    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text
    