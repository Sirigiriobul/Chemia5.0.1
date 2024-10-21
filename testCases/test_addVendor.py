import time
import string
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
from pages.addvendor import AddVendor
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
#@pytest.mark.run(order=3)
class Test_03_AddVendor:
    logger = logMaker.logGenerator()
    #@pytest.mark.order(4)
    @pytest.mark.run(order=4)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addVendor(self,setUp):
        self.logger.info("*****Test_03_Add_Vendor_started*****")
        self.driver = setUp
        self.addVendor=AddVendor(self.driver)
        self.driver.implicitly_wait(10)
        self.addVendor.click_on_main_menu()
        self.addVendor.click_on_sub_menu()
        self.addVendor.click_on_vendor_tab()
        time.sleep(4)
        self.addVendor.click_on_add_button()
        #materialCode = self.generate_random_code()
        #self.add_material.enter_material_code(materialCode)
        vendorCode=self.generate_dynamic_vendor_code()
        self.addVendor.enter_vendor_code(vendorCode)
        self.addVendor.enter_vendor_name("obulesh")
        self.addVendor.enter_description("Adding New vendor")
        self.driver.save_screenshot(".\screenshots\addVendorPopUp.png")
        self.addVendor.click_on_cancel_button()

    def generate_dynamic_vendor_code(self):
        venCode= ''.join(random.choices(string.ascii_lowercase+string.digits,k=3))
        #materialCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        return f'obulVen{venCode}'


'''
import time
import string
import random
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
from pages.addvendor import AddVendor
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker


class Test_03_Addvendor:
    admin_page_url = ReadConfig.get_AdminURL()
    userName = ReadConfig.get_userName()
    password = ReadConfig.get_password()
    logger = logMaker.logGenerator()

    @pytest.mark.run(order=4)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addVendor(self,setUp):
        self.logger.info("*****Test_03_Add_Vendor_started*****")
        self.driver = setUp
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.enter_userName(self.userName)
        self.login.enter_Password(self.password)
        self.login.clicking_on_login()
        self.logger.info("*****Test_03_has started*****")
        self.driver.save_screenshot(".\screenshots\DashboardPage.png")
        self.logger.info("*****navigated to dashboard*****")
        self.add_vendor = AddVendor(self.driver)
        self.login.clicking_on_labInventory()
        time.sleep(5)
        self.add_vendor.click_on_main_menu()
        self.add_vendor.click_on_sub_menu()
        self.add_vendor.click_on_vendor_tab()
        time.sleep(4)
        self.add_vendor.click_on_add_button()
        #materialCode = self.generate_random_code()
        #self.add_material.enter_material_code(materialCode)
        vendorCode=self.generate_dynamic_vendor_code()
        self.add_vendor.enter_vendor_code(vendorCode)
        self.add_vendor.enter_vendor_name("obulesh")
        self.add_vendor.enter_description("Adding New vendor")
        self.driver.save_screenshot(".\screenshots\addVendorPopUp.png")
        self.add_vendor.click_on_cancel_button()

    def generate_dynamic_vendor_code(self):
        venCode= ''.join(random.choices(string.ascii_lowercase+string.digits,k=3))
        #materialCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        return f'obulVen{venCode}'

'''

















