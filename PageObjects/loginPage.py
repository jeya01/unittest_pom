from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//*[@name='username']"
    textbox_password_xpath = "//*[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    #link_logout_linktext = "Logout"
    text_title = "OrangeHRM"

    def __init__(self, driver): # This is invoked whenever an object is created for thiss class
        self.driver = driver



    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath)
        #self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        #self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def ClickLogout(self):
         self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
