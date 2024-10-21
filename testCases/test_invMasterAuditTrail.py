import time
import pytest
from pages.invMasterDataAuditTrail import InvMasterDataAuditTrail
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
#@pytest.mark.run(order=5)
class Test_05_InvMasterAuditTrail:
    logger = logMaker.logGenerator()

    @pytest.mark.run(order=6)
    def test_auditTrail(self, setUp):
        self.logger.info("********Audit Trail Test Started***********")
        self.driver = setUp
        self.audit=InvMasterDataAuditTrail(self.driver)
        time.sleep(5)
        self.audit.click_on_main_menu()
        self.audit.click_on_submenu()
        self.audit.click_on_audit_trail()
        self.audit.click_on_go_button()
        time.sleep(10)






