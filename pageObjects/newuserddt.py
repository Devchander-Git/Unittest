from selenium.webdriver.common.by import By


class newuserDDT():
    button_signup_xpath ="//a[normalize-space()='Signup / Login']"
    txt_email_xpath="//input[@data-qa='login-email']"
    txt_password_xpath = "//input[@placeholder='Password']"
    button_submit_xpath="//button[normalize-space()='Login']"
    txt_msg_xpath="//h2[normalize-space()='Category']"
    button_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def signup(self):
        self.driver.find_element(By.XPATH,self.button_signup_xpath).click()

    def usremail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def userpass(self,pwd):

        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def submit(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

    def istargetpagediplayed(self):
        self.driver.find_element(By.XPATH,self.txt_msg_xpath).is_displayed()



    def logOut(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()