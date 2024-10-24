
import time
import pytest
from pages.login import Login
from pages.vendorMapping import VendorMapping
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
#@pytest.mark.run(order=4)
class Test_04_VendorMapping:
    logger = logMaker.logGenerator()
    #@pytest.mark.order(4)

    @pytest.mark.run(order=5)
    @pytest.mark.sanity
    def test_vendor_mapping(self, setUp):
        self.logger.info("********Vendor Mapping Test Started***********")
        self.driver = setUp
        self.venMap=VendorMapping(self.driver)
        time.sleep(5)
        self.venMap.click_on_main_menu()
        self.venMap.click_on_sub_menu()
        self.venMap.click_on_vendor_mapping()
        time.sleep(5)
      #  self.venMap.click_on_add_button()

    ''' self.venMap.enter_Material_Code("materialCode")
        self.driver.save_screenshot("./screenshots/vendorMapping.png")'''




'''import time
import string
import random
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.addMaterial import addMaterial
from pages.login import Login
from pages.vendorMapping import VendorMapping
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker
from testCases.test_addMaterial import addMaterial

@pytest.mark.usefixtures("setUp")
class Test_04_VendorMapping:
    admin_page_url=ReadConfig.get_AdminURL()
    userName=ReadConfig.get_userName()
    password=ReadConfig.get_password()
    logger=logMaker.logGenerator()

    @pytest.mark.run(order=5)
    @pytest.mark.sanity
    def test_vendorMapping(self,setUp):
        self.logger("********vendor_Mapping_has_Started***********")
        self.driver = setUp
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.enter_userName(self.userName)
        self.login.enter_Password(self.password)
        self.login.clicking_on_login()
        self.vendorMap = VendorMapping(self.driver)
        self.login.clicking_on_labInventory()
        time.sleep(5)
        self.vendorMap.click_on_main_menu()
        self.vendorMap.click_on_sub_menu()
        self.vendorMap.click_on_vendor_mapping()
        self.vendorMap.click_on_add_button()
        self.vendorMap.enter_material_code("materialCode")



'''






