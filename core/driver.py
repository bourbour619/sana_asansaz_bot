# This Python file uses the following encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import schema

class SanaHoghooghiDriver:

    URL: str = 'https://adliran.ir/'

    def __init__(self, person: schema.SanaHoghooghiPerson):
        self.driver = webdriver.Firefox()
        if person is None:
            # todo: must refactor
            raise Exception('Person(SanaHoghooghiPerson) Required')
        self.person = person

    def login(self):
        try:
            self.driver.get(self.URL)
            hoghooghi_tag = self.driver.find_element(By.PARTIAL_LINK_TEXT, "سامانه خودکاربری اشخاص حقوقی")
            hoghooghi_tag.click()
            WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            WebDriverWait(self.driver, 5).until(EC.url_changes(self.driver.current_url))
            code_melli_tag = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located)
            print("New URL:", self.driver.current_url)
            WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return window.angular.element(document.body).injector().get('$http').pendingRequests.length === 0"))
            code_melli_tag = self.driver.find_element(By.NAME, "personNationalCode")
            code_melli_tag.send_keys(self.person.code_melli)
            personal_password_tag = self.driver.find_element(By.NAME, "personUserPassword")
            personal_password_tag.send_keys(self.person.personal_passwrod)
            legalIdentity_tag = self.driver.find_element(By.NAME, "legalIdentity")
            legalIdentity_tag.send_keys(self.person.shenase)
            next_button_label = self.driver.find_element(By.XPATH, "//*[contains(text(), 'مرحله بعد')]")
            next_button = next_button_label.find_element(By.XPATH, '..')
            next_button.click()
            self.driver.implicitly_wait(5)
            otpPassowrd_tag = self.driver.find_element(By.NAME, "otpPassowrd")
            otpPassowrd_tag.send_keys(self.person.temp_code)
            login_button_label = self.driver.find_element(By.XPATH, "//*[contains(text(), 'ورود به سامانه')]")
            login_button = login_button_label.find_element(By.XPATH, '..')
            login_button.click()
            self.driver.quit()
        except Exception as e:
            print(e)



if __name__ == '__main__':
    _person = schema.SanaHoghooghiPerson(
        code_melli='2710166739',
        personal_passwrod='1359150119',
        shenase='14003310396',
        temp_code='879355'
    )
    _driver = SanaHoghooghiDriver(_person)
    _driver.login()
