from selenium.webdriver.common.by import By


class subscribtion():
    txt_mailId_xpath="//input[@id='susbscribe_email']"
    clk_arrow_xpath="//i[@class='fa fa-arrow-circle-o-right']"




    def __init__(self,driver):
        self.driver=driver


    def scrolldown(self):
            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            self.value = self.driver.execute_script("return window.pageYOffset;")

    def setmailId(self,mail):
        self.driver.find_element(By.XPATH,self.txt_mailId_xpath).send_keys(mail)

    def clkarrow(self):
        self.driver.find_element(By.XPATH,self.clk_arrow_xpath).click()



