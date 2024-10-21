from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    textBox_userName_id="form2Example17"
    textBox_password_id="form2Example27"
    button_login_Xpath="//button[@class='btn btn-dark btn-lg btn-block grn']"
    image_Lie_Xpath="//img[@alt='Lab-Equipment-Inventory image not found']"
    def __init__(self, driver):
        self.driver = driver

    # def enterUsername(self, username):
    #     user = WebDriverWait(self.driver, 30).until(
    #         EC.presence_of_element_located(self.username_locator)
    #     )
    #     user.click()
    #     user.send_keys(username)
    def enter_userName(self,userName):
        user=WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.ID,self.textBox_userName_id))
            )
        user.click()
        user.send_keys(userName)
    def enter_passWord(self,passWord):
        passW=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID,self.textBox_password_id))
            )
        passW.click()
        passW.send_keys(passWord)

    def clicking_on_login(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()

    def clicking_on_labInventory(self):
        self.driver.find_element(By.XPATH,self.image_Lie_Xpath).click()






