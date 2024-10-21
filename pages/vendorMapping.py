from selenium.webdriver.common.by import By

class VendorMapping:
    menu_id = "sidebar-toggle"
    submenu_InvMasterdata_Xpath = "//span[text()='Inv Master Data']"
    submenu_vendorMapping_Xpath = "//ul[@class='dropdown-menu ng-star-inserted']/child::li[3]"
    button_add_Xpath = "//mat-icon [@id='add'][1]"
    textBox_materialCode_xpath="//p-autocomplete[@formcontrolname='matCode']"
    textBox_materialName_Xpath="//span[@class='ng-tns-c135-13 p-autocomplete p-component']"
    button_save_Xpath="//span[text()=' Save ']"
    button_cancel_Xpath="//span[text()=' Cancel ']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_main_menu(self):
       self.driver.find_element(By.ID,self.menu_id).click()

    def click_on_sub_menu(self):
       self.driver.find_element(By.XPATH,self.submenu_InvMasterdata_Xpath).click()

    def click_on_vendor_mapping(self):
        self.driver.find_element(By.XPATH,self.submenu_vendorMapping_Xpath).click()

    def click_on_add_button(self):
        self.driver.find_element(By.XPATH,self.button_add_Xpath).click()
    def enter_Material_Code(self,materialCode):
        self.driver.find_element(By.XPATH,self.textBox_materialCode_xpath).send_keys(materialCode)
    def enter_Material_Name(self,materialName):
        self.driver.find_element(By.XPATH,self.textBox_materialName_Xpath).clear()
        self.driver.find_element(By.XPATH,self.textBox_materialName_Xpath).send_keys(materialName)


'''
    def enter_material_code(self,materialCode):
        self.driver.find_element(By.XPATH,self.textBox_materialCode_xpath).send_keys(materialCode)

    def enter_material_name(self,materialName):
        self.driver.find_element(By.XPATH,self.textBox_materialName_Xpath).send_keys(materialName)

    #need to add element related to vendors
    def click_on_save_button(self):
        self.driver.find_element(By.XPATH,self.button_save_Xpath)

    def click_on_cancel_button(self):
        self.driver.find_element(By.XPATH)

'''