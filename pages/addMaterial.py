from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#//p-dropdown[@formcontrolname='materialtype']//div[@class='p-dropdown p-component']
class AddMaterial:
    menu_id="sidebar-toggle"
    submenu_InvMasterdata_Xpath="//span[text()='Inv Master Data']"
    submenu_materials_Xpath="//ul[@class='dropdown-menu ng-star-inserted']/child::li[1]"
    button_add_id="add"
    materialType_selectDropdown_Xpath="//p-dropdown[@formcontrolname='materialtype']//div[@class='p-dropdown p-component']"
    dropDown_rawMaterial_Xpath="//li[@aria-label='RAW MATERIAL']"
    textBox_code_Xpath="//input[@formcontrolname='materialcode']"
    textBox_materialName_Xpath="//input[@formcontrolname='materialname']"
    textBox_abbreviation_Xpath="//input[@formcontrolname='materialshortcode']"
    uom_select_Xpath="//p-dropdown[@formcontrolname='uom']"
    dropDown_uomGm_Xpath="//li[@aria-label='gm']"
    textBox_alertLevl_Xpath="//input[@formcontrolname='alertlevel']"
    textBox_technicalGrade_Xpath="//input[@formcontrolname='technicalgrade']"
    textBox_storageCondition_Xpath="//input[@formcontrolname='storagecondition']"
    textBox_specification_Xpath="//input[@formcontrolname='specification']"
    checkBox_allowedUom_Xpath="//label[@for='nb0']"
    checkBox_hazardous_Xpath="//mat-checkbox[@formcontrolname='hazardous']"
    textBox_description_Xpath="//textarea[@formcontrolname='description']"
    textBox_precautions_Xpath="//textarea[@formcontrolname='precautions']"
    button_save_Xpath="//span[text()=' Save ']"
    button_cancel_Xpath="//span[text()=' Cancel ']"
    
    def __init__(self, driver):
        self.driver = driver

    def click_on_main_menu(self):
        self.driver.find_element(By.ID, self.menu_id).click()

    def click_on_sub_menu(self):
        self.driver.find_element(By.XPATH,self.submenu_InvMasterdata_Xpath).click()

    def click_on_material_tab(self):
        self.driver.find_element(By.XPATH,self.submenu_materials_Xpath).click()

    def click_on_Add_button(self):
        self.driver.find_element(By.ID,self.button_add_id).click()

    def click_on_material_type_dropDown(self):
        self.driver.find_element(By.XPATH,self.materialType_selectDropdown_Xpath).click()
    def click_on_raw_material(self):
        self.driver.find_element(By.XPATH,self.dropDown_rawMaterial_Xpath).click()

    def enter_material_code(self,code):
        self.driver.find_element(By.XPATH,self.textBox_code_Xpath).send_keys(code)

    def enter_material_name(self,materialName):
        self.driver.find_element(By.XPATH,self.textBox_materialName_Xpath).send_keys(materialName)

    def enter_abbreviation(self,abbreviation):
        self.driver.find_element(By.XPATH,self.textBox_abbreviation_Xpath).send_keys(abbreviation)

    def select_uom(self):
        self.driver.find_element(By.XPATH,self.uom_select_Xpath).click()

    def click_on_gm(self):
        self.driver.find_element(By.XPATH,self.dropDown_uomGm_Xpath).click()


    def enter_alert_level(self,alertLevel):
        self.driver.find_element(By.XPATH,self.textBox_alertLevl_Xpath).send_keys(alertLevel)

    def enter_tech_grade(self,techGrade):
        self.driver.find_element(By.XPATH, self.textBox_technicalGrade_Xpath).send_keys(techGrade)

    def enter_storage_condition(self,storageCondition):
        self.driver.find_element(By.XPATH, self.textBox_storageCondition_Xpath).send_keys(storageCondition)

    def enter_specification(self,Specs):
        self.driver.find_element(By.XPATH, self.textBox_specification_Xpath).send_keys(Specs)

    def select_allowed_uom(self):
        self.driver.find_element(By.XPATH, self.checkBox_allowedUom_Xpath).click()

    def enter_hazarous(self,):
        self.driver.find_element(By.XPATH, self.checkBox_hazardous_Xpath).click()

    def enter_description(self,description):
        self.driver.find_element(By.XPATH, self.textBox_description_Xpath).send_keys(description)

    def enter_precaution(self,precaution):
        self.driver.find_element(By.XPATH, self.textBox_precautions_Xpath).send_keys(precaution)

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH, self.button_save_Xpath).click()

    def click_on_cancel_button(self):
        self.driver.find_element(By.XPATH, self.button_cancel_Xpath).click()








