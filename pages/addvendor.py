from selenium.webdriver.common.by import By

class AddVendor:
    menu_id = "sidebar-toggle"
    submenu_InvMasterdata_Xpath = "//span[text()='Inv Master Data']"
    submenu_vendors_Xpath="//ul[@class='dropdown-menu ng-star-inserted']/child::li[2]"
    button_add_id = "add"
    textBox_vendorCode_Xpath="//input[@formcontrolname='vendorCode']"
    textBox_vendorName_Xpath="//input[@formcontrolname='vendorName']"
    textBox_description_Xpath= "//textarea[@formcontrolname ='vendorDesc']"
    button_Save_Xpath="//span[text()=' Save ']"
    button_cancel_Xpath="//span[text()=' Cancel ']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_main_menu(self):
        self.driver.find_element(By.ID, self.menu_id).click()

    def click_on_sub_menu(self):
        self.driver.find_element(By.XPATH, self.submenu_InvMasterdata_Xpath).click()

    def click_on_vendor_tab(self):
        self.driver.find_element(By.XPATH, self.submenu_vendors_Xpath).click()

    def click_on_add_button(self):
        self.driver.find_element(By.ID, self.button_add_id).click()

    def enter_vendor_code(self,venCode):
        self.driver.find_element(By.XPATH,self.textBox_vendorCode_Xpath).send_keys(venCode)

    def enter_vendor_name(self,vendorName):
        self.driver.find_element(By.XPATH, self.textBox_vendorName_Xpath).send_keys(vendorName)

    def enter_description(self,description):
        self.driver.find_element(By.XPATH, self.textBox_description_Xpath).send_keys(description)

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH, self.button_Save_Xpath).click()

    def click_on_cancel_button(self):
        self.driver.find_element(By.XPATH, self.button_cancel_Xpath).click()
