from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class registerUser():
    clk_signup_xpath="//a[normalize-space()='Signup / Login']"
    clk_newuserName_xpath="//input[@placeholder='Name']"
    clk_Email_xpath="//input[@data-qa='signup-email']"
    clk_submit_xpath="//button[normalize-space()='Signup']"
    txt_confirmmsg_xpath="//b[normalize-space()='Enter Account Information']"

    def __init__(self,driver):
        self.driver=driver

    def setSignup(self):
        self.driver.find_element(By.XPATH,self.clk_signup_xpath).click()

    def setNewUser(self,name):
        self.driver.find_element(By.XPATH,self.clk_newuserName_xpath).send_keys(name)

    def setEmail(self,mailId):
        self.driver.find_element(By.XPATH,self.clk_Email_xpath).send_keys(mailId)

    def submit(self):
        self.driver.find_element(By.XPATH,self.clk_submit_xpath).click()

    # def confirm_text(self):
    #     try:
    #         return self.driver.find_element(By.XPATH, self.txt_confirmmsg_xpath).text
    #
    #     except:
    #         None


