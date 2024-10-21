from selenium.webdriver.common.by import By


class InstrumentType:
    menu_id = "sidebar-toggle"
    submenu_EquipMasterdata_Xpath = "//span[text()='Equip Master Data']"
    submenu_instrumentType_Xpath = "//ul[@class='dropdown-menu ng-star-inserted']/li[1]"
    button_add_id = "add"
    textBox_instrumentType_Xpath="//input[@formcontrolname='instrTye']"
    movable_dropDown_Xpath="//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"
    select_Yes_Xpath = "//li[@aria-label='Yes']"
    description_textBox_Xpath = "//textarea[@formcontrolname='instrdesc']"
    button_save_Xpath = "//span[text()=' Save ']"
    button_cancel_Xpath = "//span[text()=' Cancel ']"

    def __init__(self,driver):
        self.driver=driver
    def clicking_menu(self):
        self.driver.find_element(By.ID,self.menu_id).click()

    def clicking_submenu_EquipMasterData(self):
        self.driver.find_element(By.XPATH,self.submenu_EquipMasterdata_Xpath).click()
    def clicking_on_submenu_instrument_menu(self):
        self.driver.find_element(By.XPATH,self.submenu_instrumentType_Xpath).click()

    def clicking_on_add_button(self):
        self.driver.find_element(By.ID,self.button_add_id).click()

    def entering_instrumenttype(self,insType):
        self.driver.find_element(By.XPATH,self.entering_instrumenttype).send_keys(insType)

    def clicking_on_movable_dropDown(self):
        self.driver.find_element(By.XPATH,self.movable_dropDown_Xpath).click()

    def selecting_yes(self):
        self.driver.find_element(By.XPATH,self.select_Yes_Xpath).click()

    def entering_description(self,description):
        self.driver.find_element(By.XPATH,self.description_textBox_Xpath).send_keys(description)

    def clicking_on_save_button(self):
        self.driver.find_element(By.XPATH,self.button_save_Xpath).click()

    def clicking_on_cancel_button(self):
        self.driver.find_element(By.XPATH,self.button_cancel_Xpath).click()







