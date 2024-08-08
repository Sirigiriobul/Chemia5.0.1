import random
import string
import time
import pytest
from pages.login import Login
from pages.addEquipmentType import AddEquipmentType
from utilities.customLogger import logMaker
from utilities.readProperties import ReadConfig
from pages.addEquipmentType import AddEquipmentType

@pytest.mark.usefixtures("setUp")
class Test_05_AddEquipmentType:
    admin_page_url=ReadConfig.get_AdminURL()
    userName=ReadConfig.get_userName()
    password=ReadConfig.get_password()
    logger=logMaker.logGenerator()

    def test_add_equipment(self,setUp):
        self.logger.info("******Add equipment is started*********")
        self.driver=setUp
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.enter_userName(self.userName)
        self.login.enter_Password(self.password)
        self.login.clicking_on_login()
        self.logger.info("*****Logged into application*****")
        self.equip_type= AddEquipmentType(self.driver)
        self.login.clicking_on_labInventory()
        time.sleep(5)
        self.equip_type.click_on_main_menu()
        self.equip_type.click_on_sub_menu()
        self.equip_type.click_on_equipment_type()
        self.equip_type.click_on_add_button()
        equip_generate_type=self.generate_random_equip_type()
        self.equip_type.entering_equipment_type(equip_generate_type)
        self.equip_type.selecting_movable()
        self.equip_type.entering_description("description is added")

        def generate_random_equip_type(self):
            equipType=''.join(random.choices(string.ascii_lowercase+string.digits,k=3))
            return f'equip{equipType}'



