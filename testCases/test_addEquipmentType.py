
import random
import string
import time
import pytest
from pages.addEquipmentType import AddEquipmentType
from utilities.customLogger import logMaker
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setUp")
@pytest.mark.usefixtures(order=6)
class Test_05_AddEquipmentType:
    logger=logMaker.logGenerator()

    @pytest.mark.run(order=7)
    def test_add_equipment_cancel_button(self,setUp):
        self.logger.info("******Add equipment is started*********")
        self.driver=setUp
        self.driver.implicitly_wait(10)
        self.addEquip=AddEquipmentType(self.driver)
        self.addEquip.click_on_main_menu()
        self.addEquip.click_on_sub_menu()
        self.addEquip.click_on_equipment_type()
        time.sleep(2)
        self.addEquip.click_on_add_button()
        time.sleep(2)
        self.addEquip.clicking_on_Cancel_button()

    @pytest.mark.run(order=8)
    def test_add_equipment(self, setUp):
        self.logger.info("******Add equipment is started*********")
        self.driver = setUp
        self.driver.implicitly_wait(10)
        self.addEquip = AddEquipmentType(self.driver)
        self.addEquip.click_on_add_button()
        self.addEquip.click_on_equipment_type()
        equipment_type=self.generate_random_equip_type()
        self.addEquip.entering_equipment_type(equipment_type)
        self.addEquip.selecting_movable()
        self.addEquip.selecting_yes()
        self.addEquip.entering_description("description is added")
        time.sleep(2)

    def generate_random_equip_type(self):
        equipment_type=''.join(random.choices(string.ascii_lowercase+string.digits,k=3))
        return f'equip{equipment_type}'



