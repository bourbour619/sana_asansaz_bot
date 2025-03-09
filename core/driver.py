import os
import time
import logging
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as se_exc

if __package__ == 'core':
    from . import models, schemas, database
else :
    import models, schemas, database
    


load_dotenv()

class SanaHoghooghiDriver:

    _URL: str = 'https://adliran.ir/'
    _BRANCHES_TREE = (
    "قوه قضائیه", [
        ("ديوان عدالت اداري", [
            ("معاونت قضايي امور اداري استخدامي و فرهنگي", [
                ("معاونت قضايي امور اداري استخدامي و فرهنگي (شعب اجراي احكام)", [
                    ("شعبه 3 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 4 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 5 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 6 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 7 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 8 اجراي احكام ديوان عدالت اداري", []),
                ]),
                ("معاونت قضايي امور اداري استخدامي و فرهنگي (شعب بدوي)", [
                    ("شعبه 24 ديوان عدالت اداري", []),
                    ("شعبه 25 ديوان عدالت اداري", []),
                    ("شعبه 26 ديوان عدالت اداري", []),
                    ("شعبه 27 ديوان عدالت اداري", []),
                    ("شعبه 28 ديوان عدالت اداري", []),
                    ("شعبه 29 ديوان عدالت اداري", []),
                    ("شعبه 30 ديوان عدالت اداري", []),
                    ("شعبه 31 ديوان عدالت اداري", []),
                    ("شعبه 32 ديوان عدالت اداري", []),
                    ("شعبه 34 ديوان عدالت اداري", []),
                    ("شعبه 35 ديوان عدالت اداري", []),
                    ("شعبه 36 ديوان عدالت اداري", []),
                    ("شعبه 37 ديوان عدالت اداري", []),
                    ("شعبه 38 ديوان عدالت اداري", []),
                    ("شعبه 39 ديوان عدالت اداري", []),
                    ("شعبه 40 ديوان عدالت اداري", []),
                    ("شعبه 41 ديوان عدالت اداري", []),
                    ("شعبه 42 ديوان عدالت اداري", []),
                    ("شعبه 43 ديوان عدالت اداري", []),
                    ("شعبه 44 ديوان عدالت اداري", []),
                    ("شعبه 45 ديوان عدالت اداري", []),
                ]),
                ("معاونت قضايي امور اداري استخدامي و فرهنگي (شعب تجديدنظر)", [
                    ("شعبه 23 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 24 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 25 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 26 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 27 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 28 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 29 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 30 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 31 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 32 تجديدنظر ديوان عدالت اداري", []),
                ]),
            ]),
            ("معاونت قضايي امور كار و تامين اجتماعي", [
                ("معاونت قضايي امور كار و تامين اجتماعي (شعب اجراي احكام)", [
                    ("شعبه 9 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 10 اجراي احكام ديوان عدالت اداري", []),
                    ("شعبه 11 اجراي احكام ديوان عدالت اداري", []),
                ]),
                ("معاونت قضايي امور كار و تامين اجتماعي (شعب بدوي)", [
                    ("شعبه 46 ديوان عدالت اداري", []),
                    ("شعبه 47 ديوان عدالت اداري", []),
                    ("شعبه 48 ديوان عدالت اداري", []),
                    ("شعبه 49 ديوان عدالت اداري", []),
                    ("شعبه 50 ديوان عدالت اداري", []),
                    ("شعبه 51 ديوان عدالت اداري", []),
                    ("شعبه 52 ديوان عدالت اداري", []),
                    ("شعبه 53 ديوان عدالت اداري", []),
                    ("شعبه 54 ديوان عدالت اداري", []),
                    ("شعبه 55 ديوان عدالت اداري", []),
                    ("شعبه 56 ديوان عدالت اداري", []),
                    ("شعبه 57 ديوان عدالت اداري", []),
                    ("شعبه 58 ديوان عدالت اداري", []),
                    ("شعبه 59 ديوان عدالت اداري", []),
                    ("شعبه 60 ديوان عدالت اداري", []),
                    ("شعبه 61 ديوان عدالت اداري", []),
                    ("شعبه 62 ديوان عدالت اداري", []),
                    ("شعبه 63 ديوان عدالت اداري", []),
                    ("شعبه 64 ديوان عدالت اداري", []),
                    ("شعبه 65 ديوان عدالت اداري", []),
                    ("شعبه 66 ديوان عدالت اداري", []),
                    ("شعبه 67 ديوان عدالت اداري", []),
                    ("شعبه 68 ديوان عدالت اداري", []),
                    ("شعبه 69 ديوان عدالت اداري", []),
                ]),
                ("معاونت قضايي امور كار و تامين اجتماعي (شعب تجديدنظر)", [
                    ("شعبه 12 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 13 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 14 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 15 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 16 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 17 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 18 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 19 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 20 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 21 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 22 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 41 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 42 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 43 تجديدنظر ديوان عدالت اداري", []),
                    ("شعبه 44 تجديدنظر ديوان عدالت اداري", []),
                ]),
            ]),
        ]),
    ]
)


    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.set_preference("privacy.trackingprotection.enabled", False)  # Disable tracking
        # options.set_preference("dom.webdriver.enabled", False)  # Try to bypass bot detection
        # options.set_preference("permissions.default.image", 2)  # Load all images immediately
        options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        self._driver = webdriver.Firefox(options=options)
        self._logged_in = False
        self._person = None

    def find_target_branch_path(self, target, tree=None, path=None):
        if path is None:
            path = []  # Start with an empty path

        if tree is not None:
            node_value, children = tree
        else: 
            node_value, children = self._BRANCHES_TREE

        # Add current node to path
        path.append(node_value)

        # If the current node is the target, return the path
        if node_value == target:
            return path

        # Recursively search in children
        for child in children:
            result = self.find_target_branch_path(target, child, path[:])  # Pass a copy of the path
            if result:
                return result  # Return the path when found

        return None  # Target not found

    def get_sana_perosn(self) -> schemas.SanaHoghooghiPerson:
        return self._person

    def set_sana_person(self, person: schemas.SanaHoghooghiPerson):
        if person is None:
            # todo: must refactor
            raise ValueError('person field (schemas.SanaHoghooghiPerson) required')
        self._person = person
        self.logout()

    def wait_url_change(self):
        WebDriverWait(self._driver, 5).until(
                lambda d: len(d.window_handles) > 1)
        handles = self._driver.window_handles
        self._driver.switch_to.window(handles[-1])
        WebDriverWait(self._driver, 30).until(
            EC.url_changes(self._driver.current_url))
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located)
        print("New URL:", self._driver.current_url)

    def login(self) -> bool:
        if self._logged_in:
            return True
        try:
            self._driver.get(self._URL)
            hoghooghi_tag = self._driver.find_element(
                By.PARTIAL_LINK_TEXT, "سامانه خودکاربری اشخاص حقوقی")
            hoghooghi_tag.click()
            self.wait_url_change()
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.NAME, "personNationalCode"))
            )
            national_code_input = self._driver.find_element(
                By.NAME, "personNationalCode")
            national_code_input.send_keys(self._person.national_code)
            user_password_input = self._driver.find_element(
                By.NAME, "personUserPassword")
            user_password_input.send_keys(self._person.user_password)
            legal_identity_input = self._driver.find_element(
                By.NAME, "legalIdentity")
            legal_identity_input.send_keys(self._person.legal_identity)
            time.sleep(2)
            next_button_label = self._driver.find_element(
                By.XPATH, "//*[contains(text(), 'مرحله بعد')]")
            next_button = next_button_label.find_element(By.XPATH, '..')
            next_button.click()
            self._driver.implicitly_wait(5)
            otp_password_input = self._driver.find_element(By.NAME, "otpPassowrd")
            otp_password_input.send_keys(self._person.otp_password)
            time.sleep(2)
            login_button_label = self._driver.find_element(
                By.XPATH, "//span[contains(text(), 'ورود به سامانه')]")
            login_button = login_button_label.find_element(By.XPATH, '..')
            login_button.click()
            self.wait_url_change()
            self._logged_in = True
            return True
        except (se_exc.NoSuchElementException,
                se_exc.TimeoutException) as e:
            logging.exception(e, exc_info=True)
            return False

    def send_sana_item(self, index: int, item: models.SanaItem):
        # if i < 1 or item is None:
        #    raise ValueError("%s params doesn't set properly" %self.send_sana_item.__name__)
        if not self.login():
            item.sending_status = models.SanaItemSendingStatus.Sent
            item.success = False
            return
        try:
            time.sleep(2)
            # self._driver.get("https://person.adliran.ir/LegalPerson/Index")
            if index == 1:
                link = WebDriverWait(self._driver, 30).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,  "ديوان عدالت اداري"))
                )
                link.click()
                time.sleep(2)
                link2 = link.find_element(By.XPATH, "..//ul//li[contains(normalize-space(.), 'ارايه و پيگيري لايحه')]")
                actions = ActionChains(self._driver)
                actions.move_to_element(link2).perform()
                link2.click()
                btn1 = self._driver.find_element(By.XPATH, "//button[contains(normalize-space(.), 'انتخاب نمایید')]")
                btn1.click()
                option = WebDriverWait(self._driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,  "//div/a//div[text()='ارايه دلائل و مدارك']"))
                )
                option.click()
                time.sleep(2)
                btn2 = WebDriverWait(self._driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//button//div[contains(normalize-space(.),'تقدیم لایحه')]"))
                )
                btn2.click()
                time.sleep(2)
            elif index > 1:
                btn1 = self._driver.find_element(By.XPATH, "//button[contains(normalize-space(.), 'لایحه جدید')]")
                btn1.click()
                time.sleep(1)
                
                alert = self._driver.find_element(By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']")
                yes_btn = alert.find_element(By.XPATH, ".//button[text()='بلی']")
                yes_btn.click()
                time.sleep(2)
                
            btn3 = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='box']//div//h5[text()='ثبت و ويرايش لايحه']"))
            )
            btn3.click()
            time.sleep(2)
            if index == 1:
                btn4 = WebDriverWait(self._driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(normalize-space(.),'افزودن')]"))
                )
                btn4.click()
            elif index > 1:
                btn4 = self._driver.find_element(By.XPATH, "//button[contains(., 'موضوع')]")
                btn4.click()
                option = self._driver.find_element(By.XPATH,  "//div/a//div[text()='ارايه دلائل و مدارك']")
                option.click()
            time.sleep(1)
            btn5 = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(normalize-space(.),'مرحله ی بعدی')]"))
            )
            btn5.click()
            input_parent = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div//label[contains(.,'شعبه رسیدگی کننده و شماره بایگانی')]/.."))
            )
            input_parent = self._driver.find_element(By.XPATH, "//div//label[contains(.,'شعبه رسیدگی کننده و شماره بایگانی')]/..")
            input_parent.find_element(By.XPATH, './/input').click()
            time.sleep(1)
            btn6 = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='btnSearchUnit']"))
            )
            btn6.click()
            # فهرست واحد های قضایی
            modal = WebDriverWait(self._driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(normalize-space(.), 'فهرست واحد های قضایی')]/ancestor::div[@class='modal-content'][last()]"))
            )
            item_branch = f'شعبه {item.branch} ديوان عدالت اداري'
            if 'اجرای احکام' in item_branch:
                item_branch = item_branch.replace(' اجرای احکام', ' اجراي احكام')
            elif 'تجدیدنظر' in item_branch:
                item_branch = item_branch.replace(' تجدیدنظر', ' تجديدنظر')
            else:
                item_branch = item_branch.replace(' بدوی', '')
            path = self.find_target_branch_path(target=item_branch)
            if path is not None:
                i = 0
                while i < len(path) :
                    try:
                        element = WebDriverWait(modal, 10).until(
                            EC.presence_of_element_located((By.XPATH, f"//div[text()='{path[i]}']"))
                        )
                        self._driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                        time.sleep(1)
                        if path[i] != item_branch:
                            element.click()
                        else:
                            element.find_element(By.XPATH, "..//input").click()
                        i += 1
                    except se_exc.StaleElementReferenceException:
                        continue

            close_btn = modal.find_element(By.XPATH, "//button[contains(normalize-space(.), 'تایید و بستن')]")
            close_btn.click()
            item.sending_status = models.SanaItemSendingStatus.Sent
            item.success = True
            time.sleep(2)
        except (se_exc.NoSuchElementException,
                se_exc.TimeoutException) as e:
            logging.exception(e, exc_info=True)

    def logout(self):
        if self._logged_in:
            btn = self._driver.find_element(By.XPATH, "//a[@tooltip='خروج از سامانه']")
            btn.click()
            time.sleep(1)
            self._logged_in = False

# For test
if __name__ == '__main__':
    _person = schemas.SanaHoghooghiPerson(
        national_code=os.getenv('SABA_PERSON_NATIONAL_CODE'),
        user_password=os.getenv('SABA_PERSON_USER_PASSWORD'),
        legal_identity=os.getenv('SABA_PERSON_LEGAL_IDENTITY'),
        otp_password=os.getenv('SABA_PERSON_OTP_PASSWORD')
    )
    _driver = SanaHoghooghiDriver()  
    _driver.set_sana_person(_person)  
    db = database.DB()
    with db.get_session() as session:
        item = session.query(models.SanaItem).first()
        _driver.send_sana_item(index=1, item=item)
        _driver.send_sana_item(index=2, item=item)