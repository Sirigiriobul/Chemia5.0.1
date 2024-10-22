import random
import time
import string

import pytest

from pages.addInstrumentType import InstrumentType
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
@pytest.mark.usefixtures(order=7)
class Test_06_addInstrument:
    logger=logMaker.logGenerator()

    @pytest.mark.run(order=2)
    def test_add_instrument_cancel_button(self, setUp):
        self.logger.info("******Add instrument is started*********")
        self.driver = setUp
        self.driver.implicitly_wait(10)
        self.addIns = InstrumentType(self.driver)
        self.addIns.click_on_main_menu()
        self.addIns.click_on_equipMasterData_subMenu()
        self.addIns.clicking_on_submenu_instrument_menu()
        time.sleep(2)
        self.addIns.clicking_on_add_button()
        time.sleep(2)
        self.addIns.clicking_on_cancel_button()

    @pytest.mark.run(order=3)
    def test_add_instrumentType(self, setUp):
        self.logger.info("******Add instrument type is started*********")
        self.driver = setUp
        self.driver.implicitly_wait(10)
        self.addIns = InstrumentType(self.driver)
        self.addIns.click_on_main_menu()
        self.addIns.click_on_equipMasterData_subMenu()
        self.addIns.clicking_on_submenu_instrument_menu()
        time.sleep(2)
        self.addIns.clicking_on_add_button()
        time.sleep(2)
        ins_type = self.generate_random_instrument_type()
        self.addIns.click_on_instrumenttype(ins_type)
        self.addIns.clicking_on_movable_dropDown()
        self.addIns.selecting_yes()
        self.addIns.entering_description("description is added")
        time.sleep(2)

    def generate_random_instrument_type(self):
        instrument_type = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        return f'instrument{instrument_type}'


