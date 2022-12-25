import unittest

import time

import HtmlTestRunner

from PageObjects.loginPage import LoginPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    '''class variables'''
    driver = None

    # opt = webdriver.ChromeOptions() # Chrome options is used to mnipulate various properties in chrome driver

    '''The solution involves the use of excludeSwitches – 
    these are switches / flags that you want to exclude ChromeDriver from including by default.
     So, anything passed through excludeSwitches basically negates / removes a flag normally set as true by ChromeDriver.
    Turns out, ChromeDriver has a default switch that enables logging 
    enable-logging; you need to pass this to Selenium to turn it off. '''

    # opt.add_experimental_option('excludeSwitches', ['enable-logging'])  # i have got usb error to remove the error i used this line
    # driver = webdriver.Chrome(options=opt)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        cls.driver.get(baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        username = "Admin"
        password = "admin123"
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.ClickLogin()
        time.sleep(5)
        self.assertEqual("OrangeHRM", self.driver.title)
        # self.lp.ClickLogout()

    @classmethod
    def tearDownClass(cls) -> None:  # none means when we dont return anything
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
'''
# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
#     output="D:\\PycharmProjects\\PythonUnittest_POM\\Reports"))
# Report is geneated i removed the keyword unittest when executing the script in command line
# python -m Testcases.test_login
'''