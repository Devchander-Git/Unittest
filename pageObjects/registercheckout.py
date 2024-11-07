from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class registerCheckout():

    #Login Process

    clk_signIn_xpath="//a[normalize-space()='Signup / Login']"
    txt_email_xpath="//input[@data-qa='login-email']"
    txt_password_xpath="//input[@data-qa='login-password']"
    clk_login_xpath="//button[@data-qa='login-button']"

    #Add Product

    clk_product_xpath="//a[@href='/products']"
    hover_product1_css="//div[3]//div[1]//div[1]//div[2]"
    hover_product1cart_css="//div[3]//div[1]//div[1]//div[2]//div[1]//a[1]"
    verify_added_xpath="//h4[normalize-space()='Added!']"
    clk_continue_xpath="//button[@data-dismiss='modal']"
    hover_product2_xpath="//div[4]//div[1]//div[1]//div[2]"
    hover_product2cart_xpath="//div[4]//div[1]//div[1]//div[2]//div[1]//a[1]"
    clk_vewcart_xpath="//a[@href='/view_cart']"



    def __init__(self,driver):
        self.driver=driver
        self.act=ActionChains(self.driver)

    def signIn(self):
        self.driver.find_element(By.XPATH,self.clk_signIn_xpath).click()

    def userEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def password(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def login(self):
        self.driver.find_element(By.XPATH,self.clk_login_xpath).click()

    def clkproduct(self):
        self.driver.find_element(By.XPATH,self.clk_product_xpath).click()
    def product1(self):
        self.prdt1=self.driver.find_element(By.XPATH,self.hover_product1_css)
        self.act.move_to_element(self.prdt1).click().perform()

    def prdtCart1(self):
        self.cart1=self.driver.find_element(By.XPATH,self.hover_product1cart_css)
        self.act.move_to_element(self.cart1).click().perform()

    def clkcontinue(self):
        self.driver.find_element(By.XPATH,self.clk_continue_xpath).click()

    def product2(self):
        self.prdt2=self.driver.find_element(By.XPATH,self.hover_product2_xpath)
        self.act.move_to_element(self.prdt2).click().perform()

    def product2cart(self):
        self.prdt2cart=self.driver.find_element(By.XPATH,self.hover_product2cart_xpath)
        self.act.move_to_element(self.prdt2cart).click().perform()
    def verification(self):

        return self.driver.find_element(By.XPATH,self.verify_added_xpath).text
    def viewcart(self):
        self.driver.find_element(By.XPATH,self.clk_vewcart_xpath).click()



