from selenium.webdriver.common.by import By


class cartPage():
    clk_cart_xpath="/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]"
    txt_mailId_xpath="//input[@id='susbscribe_email']"
    clk_arrow_xpath="//i[@class='fa fa-arrow-circle-o-right']"


    def __init__(self,driver):
        self.driver=driver

    def clkcart(self):
        self.driver.find_element(By.XPATH,self.clk_cart_xpath).click()

    def setmail(self,mail):
        self.driver.find_element(By.XPATH,self.txt_mailId_xpath).send_keys(mail)

    def clkarrow(self):
        #try:
            self.driver.find_element(By.XPATH,self.clk_arrow_xpath).click()
        #except:
            #
        None
