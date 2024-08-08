import time
import string
import random
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
from pages.addMaterial import AddMaterial
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
class Test_02_AddMaterial:
    admin_page_url = ReadConfig.get_AdminURL()
    userName = ReadConfig.get_userName()
    password = ReadConfig.get_password()
    logger = logMaker.logGenerator()

    #@pytest.mark.order(3)
    @pytest.mark.run(order=3)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_adding_material(self, setUp):
        self.logger.info("*****Test_02_Add_Material_started*****")
        self.driver = setUp
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()

        # Log in to the application
        self.login = Login(self.driver)
        self.login.enter_userName(self.userName)
        self.login.enter_Password(self.password)
        self.login.clicking_on_login()
        self.logger.info("*****Test_02_Add_Material_logged into application*****")

        # Take a screenshot of the dashboard page
        self.driver.save_screenshot("./screenshots/DashboardPage.png")
        self.logger.info("*****Navigated to dashboard*****")

        # Interact with the Add Material page
        self.add_material = AddMaterial(self.driver)
        self.login.clicking_on_labInventory()
        time.sleep(5)  # Adjust timing as necessary

        self.add_material.click_on_main_menu()
        self.add_material.click_on_sub_menu()
        self.add_material.click_on_material_tab()
        time.sleep(4)  # Adjust timing as necessary

        self.add_material.click_on_Add_button()
        time.sleep(2)  # Adjust timing as necessary

        self.add_material.click_on_material_type_dropDown()
        time.sleep(1)  # Adjust timing as necessary
        self.add_material.click_on_raw_material()

        materialCode = self.generate_random_code()
        self.add_material.enter_material_code(materialCode)
        self.add_material.enter_material_name("obulesh")
        self.add_material.enter_abbreviation("ob-123")
        self.add_material.select_uom()
        time.sleep(1)  # Adjust timing as necessary

        self.add_material.click_on_gm()
        self.add_material.enter_alert_level("10")
        self.add_material.enter_tech_grade("25")
        self.add_material.enter_storage_condition("cool")
        self.add_material.select_allowed_uom()
        self.add_material.enter_hazarous()
        self.add_material.enter_description("description")
        self.add_material.enter_precaution("Handle with care")
        time.sleep(10)  # Adjust timing as necessary

        # Take screenshots of the Add Material popup and dashboard after closing the popup
        self.driver.save_screenshot("./screenshots/AddMaterialPop-up.png")
        # self.add_material.click_on_save_button()  # Uncomment if you want to save the material
        self.add_material.click_on_cancel_button()
        self.driver.save_screenshot("./screenshots/dashboardAfterClosingMaterialPop-Up.png")

    def generate_random_code(self):
        """Generate a random material code"""
        materialCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        return f'obul{materialCode}'


'''
import time
import string
import random
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
from pages.addMaterial import addMaterial
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
class Test_02_AddMaterial:
    admin_page_url=ReadConfig.get_AdminURL()
    userName=ReadConfig.get_userName()
    password=ReadConfig.get_password()
    logger=logMaker.logGenerator()

    @pytest.mark.run(order=3)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_adding_material(self,setUp):
        self.logger.info("*****Test_02_Add_Material_started*****")
        self.driver=setUp
         self.driver.implicitly_wait(20)
         self.driver.get(self.admin_page_url)
         self.driver.maximize_window()
         self.login = Login(self.driver)
         self.login.enter_userName(self.userName)
         self.login.enter_Password(self.password)
         self.login.clicking_on_login()
         self.logger.info("*****Test_02_Add_Material_logged into application*****")
         self.driver.save_screenshot(".\screenshots\DashboardPage.png")
         self.logger.info("*****navigated to dashboard*****")
         self.add_material=addMaterial(self.driver)
        self.login.clicking_on_labInventory()
        time.sleep(5)
        self.add_material.click_on_main_menu()
        self.add_material.click_on_sub_menu()
        self.add_material.click_on_material_tab()
        time.sleep(4)
        self.add_material.click_on_Add_button()
        time.sleep(2)
        self.add_material.click_on_material_type_dropDown()
        time.sleep(1)
        self.add_material.click_on_raw_material()
        materialCode= self.generate_random_code()
        self.add_material.enter_material_code(materialCode)
        self.add_material.enter_material_name("obulesh")
        self.add_material.enter_abbreviation("ob-123")
        self.add_material.select_uom()
        time.sleep(1)
        self.add_material.click_on_gm()
        self.add_material.enter_alert_level("10")
        self.add_material.enter_tech_grade("25")
        self.add_material.enter_storage_condition("cool")
        self.add_material.select_allowed_uom()
        self.add_material.enter_hazarous()
        self.add_material.enter_description("description")
        self.add_material.enter_precaution("Handle with care")
        time.sleep(10)
        self.driver.save_screenshot(".\screenshots\AddMaterialPop-up.png")
       # self.add_material.click_on_save_button()
        self.add_material.click_on_cancel_button()
        self.driver.save_screenshot(".\screenshots\dashboardAfterClosingMaterialPop-Up.png")

     #   // table // tbody // tr / td    -for getting all the rows present in the table
     #  //table//tbody//tr/td    -For getting all the columns in the page
     #  // table // tbody // tr[1] // td   ----tr[1] = table row and only
    def generate_random_code(self):  # Added self here to make it an instance method
        materialCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        return f'obul{materialCode}'



'''








