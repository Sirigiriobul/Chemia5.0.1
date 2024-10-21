import time
import pytest

from pages.login import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logMaker

@pytest.mark.usefixtures("setUp")
#@pytest.mark.run(order=1)
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
        self.driver = setUp
        self.login = Login(self.driver)
        self.driver.get(self.admin_page_url)  # Use the URL from ReadConfig
        self.driver.maximize_window()
        self.login.enter_userName(self.userName)
        self.login.enter_passWord(self.password)
        self.login.clicking_on_login()
        time.sleep(4)
        self.login.clicking_on_labInventory()
        time.sleep(5)

        expected_title = "Lab Inventory & Equipment"
        actual_title = self.driver.title

        if actual_title == expected_title:
          self.logger.info("Title matched successfully! Title: {actual_title}")
        else:
            self.logger.error("Title mismatch! Expected: {expected_title}, but got: {actual_title}")

        # Optionally, you can use an assertion instead of logging
        assert actual_title == expected_title, f"Title mismatch! Expected: {expected_title}, but got: {actual_title}"


    #pytest.mark.order(2)
    # @pytest.mark.run(order=2)
    # @pytest.mark.smoke




