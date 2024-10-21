import time
import string
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import Login
from pages.addMaterial import AddMaterial
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
#@pytest.mark.run(order=2)
class Test_02_AddMaterial:
    logger = logMaker.logGenerator()
    @pytest.mark.run(order=2)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_closing_material_popup(self, setUp):
        self.logger.info("******Empty material pop-up******")
        self.driver=setUp
        self.add = AddMaterial(self.driver)
        self.driver.implicitly_wait(20)
        # Log in to the application
        # Take a screenshot of the dashboard page
        self.driver.save_screenshot("./screenshots/DashboardPage.png")
        self.add.click_on_main_menu()
        self.add.click_on_sub_menu()
        self.add.click_on_material_tab()
        time.sleep(3)
        self.add.click_on_Add_button()
        time.sleep(2)
        self.add.click_on_cancel_button()

    @pytest.mark.run(order=3)
    def test_adding_material(self, setUp):
        self.logger.info("*****Test_02_Add_Material_started*****")
        self.driver = setUp
        self.add = AddMaterial(self.driver)
        self.driver.implicitly_wait(20)
        # Log in to the application
        # Take a screenshot of the dashboard page
        self.driver.save_screenshot("./screenshots/DashboardPage.png")
        self.add.click_on_main_menu()
        self.add.click_on_sub_menu()
        self.add.click_on_material_tab()
        time.sleep(3)
        self.add.click_on_Add_button()
        self.add.click_on_material_type_dropDown()
        self.add.click_on_raw_material()
        # Call the functions to generate values
        material_code = self.generate_random_code()
        material_name = self.generate_random_materialName()

        # Pass the generated values to the methods
        self.add.enter_material_code(material_code)
        self.add.enter_material_name(material_name)
        self.add.enter_abbreviation("Ab-123")
        self.add.select_uom()
        self.add.click_on_gm()
        self.add.enter_alert_level("10")
        self.add.enter_tech_grade("Tech-123")
        self.add.enter_storage_condition("In House")
        self.add.enter_specification("Spec")
        self.add.select_allowed_uom()
        self.add.enter_description("Description")
        self.add.enter_precaution("Precaution")
        self.add.click_on_cancel_button()

    def generate_random_code(self):
        """Generate a random material code"""
        material_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        return f'obul{material_code}'

    def generate_random_materialName(self):
        """Generate a random material name"""
        material_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f'mat{material_name}'

#          # Interact with the Add Material page
#         self.add_material = AddMaterial(self.driver)
#         self.login.clicking_on_labInventory()
#         time.sleep(5)  # Adjust timing as necessary
#         self.add_material.click_on_main_menu()
#         self.add_material.click_on_sub_menu()
#         self.add_material.click_on_material_tab()
#         time.sleep(4)  # Adjust timing as necessary
#
#         self.add_material.click_on_Add_button()
#         time.sleep(2)  # Adjust timing as necessary
#
#         self.add_material.click_on_material_type_dropDown()
#         time.sleep(1)  # Adjust timing as necessary
#         self.add_material.click_on_raw_material()
#
#         materialCode = self.generate_random_code()
#         self.add_material.enter_material_code(materialCode)
#         self.add_material.enter_material_name("obulesh")
#         self.add_material.enter_abbreviation("ob-123")
#         self.add_material.select_uom()
#         time.sleep(1)  # Adjust timing as necessary
#
#         self.add_material.click_on_gm()
#         self.add_material.enter_alert_level("10")
#         self.add_material.enter_tech_grade("25")
#         self.add_material.enter_storage_condition("cool")
#         self.add_material.select_allowed_uom()
#         self.add_material.enter_hazarous()
#         self.add_material.enter_description("description")
#         self.add_material.enter_precaution("Handle with care")
#         time.sleep(10)  # Adjust timing as necessary
#
#         # Take screenshots of the Add Material popup and dashboard after closing the popup
#         self.driver.save_screenshot("./screenshots/AddMaterialPop-up.png")
#         # self.add_material.click_on_save_button()  # Uncomment if you want to save the material
#         self.add_material.click_on_cancel_button()
#         self.driver.save_screenshot("./screenshots/dashboardAfterClosingMaterialPop-Up.png")
#
#     def generate_random_code(self):
#         """Generate a random material code"""
#         materialCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
#         return f'obul{materialCode}'''
#
#
# '''
# import time
# import string
# import random
# from selenium.webdriver.support.ui import Select
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from pages.login import Login
# from pages.addMaterial import addMaterial
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import logMaker
#
# @pytest.mark.usefixtures("setUp")
# class Test_02_AddMaterial:
#     admin_page_url=ReadConfig.get_AdminURL()
#     userName=ReadConfig.get_userName()
#     password=ReadConfig.get_password()
#     logger=logMaker.logGenerator()
#
#     @pytest.mark.run(order=3)
#     @pytest.mark.sanity
#     @pytest.mark.regression
#     def test_adding_material(self,setUp):
#         self.logger.info("*****Test_02_Add_Material_started*****")
#         self.driver=setUp
#          self.driver.implicitly_wait(20)
#          self.driver.get(self.admin_page_url)
#          self.driver.maximize_window()
#          self.login = Login(self.driver)
#          self.login.enter_userName(self.userName)
#          self.login.enter_Password(self.password)
#          self.login.clicking_on_login()
#          self.logger.info("*****Test_02_Add_Material_logged into application*****")
#          self.driver.save_screenshot(".\screenshots\DashboardPage.png")
#          self.logger.info("*****navigated to dashboard*****")
#          self.add_material=addMaterial(self.driver)
#         self.login.clicking_on_labInventory()
#         time.sleep(5)
#         self.add_material.click_on_main_menu()
#         self.add_material.click_on_sub_menu()
#         self.add_material.click_on_material_tab()
#         time.sleep(4)
#         self.add_material.click_on_Add_button()
#         time.sleep(2)
#         self.add_material.click_on_material_type_dropDown()
#         time.sleep(1)
#         self.add_material.click_on_raw_material()
#         materialCode= self.generate_random_code()
#         self.add_material.enter_material_code(materialCode)
#         self.add_material.enter_material_name("obulesh")
#         self.add_material.enter_abbreviation("ob-123")
#         self.add_material.select_uom()
#         time.sleep(1)
#         self.add_material.click_on_gm()
#         self.add_material.enter_alert_level("10")
#         self.add_material.enter_tech_grade("25")
#         self.add_material.enter_storage_condition("cool")
#         self.add_material.select_allowed_uom()
#         self.add_material.enter_hazarous()
#         self.add_material.enter_description("description")
#         self.add_material.enter_precaution("Handle with care")
#         time.sleep(10)
#         self.driver.save_screenshot(".\screenshots\AddMaterialPop-up.png")
#        # self.add_material.click_on_save_button()
#         self.add_material.click_on_cancel_button()
#         self.driver.save_screenshot(".\screenshots\dashboardAfterClosingMaterialPop-Up.png")
#
#      #   // table // tbody // tr / td    -for getting all the rows present in the table
#      #  //table//tbody//tr/td    -For getting all the columns in the page
#      #  // table // tbody // tr[1] // td   ----tr[1] = table row and only
#     def generate_random_code(self):  # Added self here to make it an instance method
#         materialCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
#         return f'obul{materialCode}'
#
#
#
# '''
#
#
#
#
#
#
#
#
