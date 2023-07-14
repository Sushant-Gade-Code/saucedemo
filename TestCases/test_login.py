import time

from selenium import webdriver

from PageObjects.LogInPage import LogInPage
from Utilities.Readproperties import ReadProperties
from Utilities.loggen import Loggen


class Test_login_001:
    url=ReadProperties.getUrl()
    UserName=ReadProperties.getUsername()
    PassWord=ReadProperties.getPassword()
    log=Loggen.loggen()

    def test_Test_HomePageTitle__001(self,setup):
        self.log.info("TestCase test_Test_HomePageTitle__001 Started..!")
        self.driver =setup
        self.log.info("Initializing driver is Done..!")
        self.driver.get(self.url)
        self.log.info("Opening Url successfully..!")
        act_title = self.driver.title
        self.log.info("Capturing Titel successfully..!")
        exp_title = "Swag Labs"
        if act_title == exp_title:
            self.log.info("TestCase test_Test_HomePageTitle__001 Passed..!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase test_Test_HomePageTitle__001Pass.png")
            self.driver.close()
            assert True
        else:
            self.log.info("TestCase test_Test_HomePageTitle__001 Failed..!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase test_Test_HomePageTitle__001Failed.png")
            assert False

    def test_login__002(self,setup):
        self.log.info("TestCase test_login__002 Started..!")
        self.driver = setup
        self.log.info("Initializing driver is Done..!")
        self.driver.get(self.url)
        self.log.info("Opening Url successfully..!")
        self.lp=LogInPage(self.driver)
        self.lp.getUserName(self.UserName)
        self.log.info("Getting Username successfully..!")
        self.lp.getPassword(self.PassWord)
        self.log.info("Getting Password successfully..!")
        self.lp.getLoginButton()
        self.log.info("Getting LogInButton successfully..!")
        act_titel=self.lp.getTitle()
        self.log.info("Capturing Titel successfully..!")
        exp_title="Products"
        if act_titel==exp_title:
            self.log.info("TestCase test_login__002 Passed..!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase test_login__002Pass.png")
            assert True

        else:
            self.log.info("TestCase test_login__002 Failed..!")
            self.driver.save_screenshot(".\\Screenshots\\TestCase test_login__002Failed.png")
            assert False
        self.driver.implicitly_wait(10)
        self.lp.getMenu()
        time.sleep(2)
        self.lp.getLogout()
        self.driver.close()


