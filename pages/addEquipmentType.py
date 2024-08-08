from selenium.webdriver.common.by import By
from pages.addMaterial import AddMaterial

class AddEquipmentType:
    menu_id = "sidebar-toggle"
    submenu_EquipMasterdata_Xpath = "//span[text()='Equip Master Data']"
    submenu_EquipmentType_Xpath = "//ul[@class='dropdown-menu ng-star-inserted']/li[1]"
    button_add_Xpath="//div[@class='panelTitle1']/mat-icon[1]"
    textBox_equipmentType_Xpath="//input[@formcontrolname='equipTye']"
    movable_dropDown_Xpath="//div[@class='p-dropdown p-component']"
    description_textBox_Xpath="//textarea[@formcontrolname='equipdesc']"
    button_save_Xpath="//span[text()=' Save ']"
    button_cancel_Xpath="//span[text()=' Cancel ']"
    
    def __init__(self,driver):
        self.driver=driver

    def click_on_main_menu(self):
        self.driver.find_element(By.ID,self.menu_id).click()

    def click_on_sub_menu(self):
        self.driver.find_element(By.XPATH,self.submenu_EquipMasterdata_Xpath).click()

    def click_on_equipment_type(self):
        self.driver.find_element(By.XPATH,self.submenu_EquipmentType_Xpath).click()

    def click_on_add_button(self):
        self.driver.find_element(By.XPATH,self.button_add_Xpath).click()

    def entering_equipment_type(self,equipmentType):
        self.driver.find_element(By.XPATH,self.textBox_equipmentType_Xpath).send_keys(equipmentType)

    def selecting_movable(self,movable):
        self.driver.find_element(By.XPATH,self.movable_dropDown_Xpath).click()

    def entering_description(self,description):
        self.driver.find_element(By.XPATH,self.description_textBox_Xpath).send_keys(description)

    def clicking_on_save_button(self):
        self.driver.find_element(By.XPATH,self.button_save_Xpath).click()

    def clicking_on_Cancel_button(self):
        self.driver.find_element(By.XPATH,self.button_cancel_Xpath).click()







