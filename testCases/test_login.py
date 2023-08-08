import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("*************** Verifying Home Page Title ***************")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** Test Passed ***************")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*************** Test Failed ***************")
            assert False

    def test_login(self, setup):
        self.logger.info("*************** Verifying Login Test ***************")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************** Test Passed ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            self.logger.info("*************** Test Failed ***************")
            assert False