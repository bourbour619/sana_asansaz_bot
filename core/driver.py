import os
import time
import logging
from dotenv import load_dotenv

from selenium import webdriver
from selenium.common import exceptions as se_exc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import schemas


load_dotenv()


class SanaHoghooghiDriver:

    URL: str = 'https://adliran.ir/'

    def __init__(self, person: schemas.SanaHoghooghiPerson):
        self.driver = webdriver.Firefox()
        if person is None:
            # todo: must refactor
            raise Exception('Person(SanaHoghooghiPerson) Required')
        self.person = person

    def login(self):
        try:
            self.driver.get(self.URL)
            hoghooghi_tag = self.driver.find_element(
                By.PARTIAL_LINK_TEXT, "سامانه خودکاربری اشخاص حقوقی")
            hoghooghi_tag.click()
            WebDriverWait(self.driver, 5).until(
                lambda d: len(d.window_handles) > 1)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            WebDriverWait(self.driver, 5).until(
                EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located)
            print("New URL:", self.driver.current_url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "personNationalCode"))
            )
            code_melli_tag = self.driver.find_element(
                By.NAME, "personNationalCode")
            code_melli_tag.send_keys(self.person.national_code)
            personal_password_tag = self.driver.find_element(
                By.NAME, "personUserPassword")
            personal_password_tag.send_keys(self.person.user_password)
            legalIdentity_tag = self.driver.find_element(
                By.NAME, "legalIdentity")
            legalIdentity_tag.send_keys(self.person.legal_identity)
            time.sleep(2)
            next_button_label = self.driver.find_element(
                By.XPATH, "//*[contains(text(), 'مرحله بعد')]")
            next_button = next_button_label.find_element(By.XPATH, '..')
            next_button.click()
            self.driver.implicitly_wait(5)
            otpPassowrd_tag = self.driver.find_element(By.NAME, "otpPassoswrd")
            otpPassowrd_tag.send_keys(self.person.otp_password)
            time.sleep(2)
            login_button_label = self.driver.find_element(
                By.XPATH, "//span[contains(text(), 'ورود به سامانه')]")
            login_button = login_button_label.find_element(By.XPATH, '..')
            login_button.click()
            WebDriverWait(self.driver, 5).until(
                lambda d: len(d.window_handles) > 1)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            WebDriverWait(self.driver, 5).until(
                EC.url_changes(self.driver.current_url))
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located)
            print("New URL:", self.driver.current_url)
            self.driver.quit()
        except (se_exc.NoSuchElementException,
                se_exc.TimeoutException) as e:
            logging.exception(e, exc_info=True)


# For test
if __name__ == '__main__':
    _person = schemas.SanaHoghooghiPerson(
        national_code=os.getenv('SABA_PERSON_NATIONAL_CODE'),
        user_password=os.getenv('SABA_PERSON_USER_PASSWORD'),
        legal_identity=os.getenv('SABA_PERSON_LEGAL_IDENTITY'),
        otp_password=os.getenv('SABA_PERSON_OTP_PASSWORD')
    )
    _driver = SanaHoghooghiDriver(_person)
    _driver.login()
