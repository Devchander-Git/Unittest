from selenium.webdriver.common.by import By


class loginPage():
    btn_signuplogin_xpath="//a[normalize-space()='Signup / Login']"
    txt_nameemail_xpath="//input[@data-qa='login-email']"
    txt_pass_xpath="//input[@placeholder='Password']"
    btn_login_xpath="//button[normalize-space()='Login']"
    txt_message_xpath="//a[normalize-space()='Delete Account']"
    btn_logedout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def signlogin(self):
        self.driver.find_element(By.XPATH,self.btn_signuplogin_xpath).click()

    def setemail(self,mailId):
        self.driver.find_element(By.XPATH,self.txt_nameemail_xpath).send_keys(mailId)

    def setpass(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_pass_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def massage(self):

            return self.driver.find_element(By.XPATH,self.txt_message_xpath).text


    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.btn_logedout_xpath).click()