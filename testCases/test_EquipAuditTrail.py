import time
import string

import pytest

from pages.equipAuditTrail import equipMasterDataAuditTrail
from utilities.customLogger import logMaker
@pytest.mark.usefixtures("setUp")
class Test_07_EquipMasterData:
    logger = logMaker.logGenerator()

    @pytest.mark.usefixtures(order=2)
    def test_EquipMasterDataAuditTrail(self,setUp):
        self.logger.info("*****Equip Audit Trail is started*********")
        self.driver=setUp
        self.driver.implicitly_wait(10)
        self.equipAudit=equipMasterDataAuditTrail(self.driver)
        self.equipAudit.click_on_main_menu()
        self.equipAudit.click_on_equip_master_data()
        self.equipAudit.click_on_audit_trail()
        self.equipAudit.click_on_go_button()
        time.sleep(5)

#Good



