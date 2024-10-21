from selenium.webdriver.common.by import By

class InvMasterDataAuditTrail:
    menu_id = "sidebar-toggle"
    submenu_invMasterdata_Xpath = "//span[text()='Inv Master Data']"
    submenu_auditTrail_Xpath="//ul[@class='dropdown-menu ng-star-inserted']/li[4]"
    go_button_Xpath="//button[@id='goButoon']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_main_menu(self):
       self.driver.find_element(By.ID, self.menu_id).click()

    def click_on_submenu(self):
        self.driver.find_element(By.XPATH,self.submenu_invMasterdata_Xpath).click()

    def click_on_audit_trail(self):
        self.driver.find_element(By.XPATH,self.submenu_auditTrail_Xpath).click()

    def click_on_go_button(self):
        self.driver.find_element(By.XPATH,self.go_button_Xpath).click()



