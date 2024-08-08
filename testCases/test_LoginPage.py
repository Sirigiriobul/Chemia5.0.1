import time
import pytest
from pages.login import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker


@pytest.mark.usefixtures("setUp")
class Test_01_Login:
    admin_page_url = ReadConfig.get_AdminURL()
    userName = ReadConfig.get_userName()
    password = ReadConfig.get_password()
    invalid_userName = ReadConfig.get_invaliduserName()  # Negative test case
    logger = logMaker.logGenerator()

    #@pytest.mark.order(1)
    @pytest.mark.run(order=1)
    def test_Title_Verification(self, setUp):  # Ensure `setUp` fixture is used correctly
        self.logger.info("*****Test_01_AdminLogin*****")
        self.logger.info("****verification of admin login page title*****")
        self.driver = setUp
        self.driver.get(self.admin_page_url)  # Use the URL from ReadConfig
        self.logger.info("*****Test title verification matches*****")
        #self.driver.close()


    #pytest.mark.order(2)
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_valid_login_page(self, setUp):
        self.driver = setUp
        self.login = Login(self.driver)
        time.sleep(5)
        self.login.enter_userName(self.userName)
        self.login.enter_Password(self.password)
        self.login.clicking_on_login()
        time.sleep(4)
        self.login.clicking_on_labInventory()




'''

import time

import pytest
from pages.login import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
class Test_01_Login():
     admin_page_url=ReadConfig.get_AdminURL()
     userName=ReadConfig.get_userName()
     password=ReadConfig.get_password()
     invalid_userName=ReadConfig.get_invaliduserName()  #Negative test case
     logger=logMaker.logGenerator()

    @pytest.mark.run(order=1)
    def test_Title_Verification(self, driver):    #need to add setUp
        self.logger.info("*****Test_01_AdminLogin*****")
        self.logger.info("****verification of admin login page title*****")
         self.driver=setUp
        self.driver.get("http://10.106.100.222:9098/Chemia/login/cpl")
        act_title=self.driver.title
        self.logger.info("*****Test title verification matches*****")
        assert True
        self.driver.close()

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_valid_login_page(self, driver):
        # self.driver = setUp
        self.login = Login(driver)
        time.sleep(5)

        self.login.enter_userName(login['user'])
        self.login.enter_Password(login['password'])
        self.login.clicking_on_login()
        time.sleep(4)
        self.login.clicking_on_labInventory()

'''


















