from selenium.webdriver.common.by import By


class existingEmail():
    btn_signlogin_xpath="//a[normalize-space()='Signup / Login']"
    txt_name_xpath="//input[@placeholder='Name']"
    txt_email_xpath="//input[@data-qa='signup-email']"
    btn_login_xpath="//button[normalize-space()='Signup']"
    txt_message_xpath="//b[normalize-space()='Enter Account Information']"



    def __init__(self,driver):
        self.driver=driver

    def setsignlogin(self):
        self.driver.find_element(By.XPATH,self.btn_signlogin_xpath).click()

    def setname(self,name):
        self.driver.find_element(By.XPATH,self.txt_name_xpath).send_keys(name)

    def setemail(self,mailId):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(mailId)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def message(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_message_xpath).text()
        except:
            None
