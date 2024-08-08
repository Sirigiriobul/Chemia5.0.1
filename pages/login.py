from selenium.webdriver.common.by import By

class Login:
    textBox_userName_id="form2Example17"
    textBox_password_id="form2Example27"
    button_login_Xpath="//button[@class='btn btn-dark btn-lg btn-block grn']"
    image_Lie_Xpath="//img[@alt='Lab-Equipment-Inventory image not found']"
    def __init__(self, driver):
        self.driver = driver

    def enter_userName(self,userName):
        self.driver.find_element(By.ID, self.textBox_userName_id).send_keys(userName)

    def enter_Password(self, Password):
        self.driver.find_element(By.ID, self.textBox_password_id).clear()
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(Password)

    def clicking_on_login(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()

    def clicking_on_labInventory(self):
        self.driver.find_element(By.XPATH,self.image_Lie_Xpath).click()


