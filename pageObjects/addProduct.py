from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains



class addProduct():
    lnk_products_xpath="//a[@href='/products']"

    clk_Istproduct_xpath="//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]"
    clk_addcart_xpath="body > section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3)"
    clk_continue_xpath="//button[@class='btn btn-success close-modal btn-block']"
    clk_IIndproduct_xpath="//div[3]//div[1]//div[1]//div[2]"
    clk_addcart1_xpath="//div[3]//div[1]//div[1]//div[2]//div[1]//a[1]"
    clk_viewcart_xpath="/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]"
    chk_checkout_xpath="//a[@class='btn btn-default check_out']"
    chk_blueTop_xpath="//a[normalize-space()='Blue Top']"
    chk_mensTshirt_xpath="//a[normalize-space()='Men Tshirt']"





    def __init__(self,driver):
        self.driver=driver
        self.act = ActionChains(self.driver)




    def clickProduct(self):
        self.driver.find_element(By.XPATH,self.lnk_products_xpath).click()




    def firstProduct(self):
        self.first=self.driver.find_element(By.XPATH,self.clk_Istproduct_xpath)

        self.act.move_to_element(self.first).perform()

    def addcart1(self):
        self.addc=self.driver.find_element(By.CSS_SELECTOR,self.clk_addcart_xpath)
        self.act.move_to_element(self.addc).click().perform()

    def continuecart(self):

        self.driver.find_element(By.XPATH,self.clk_continue_xpath).click()

    def IIproduct(self):
        self.second=self.driver.find_element(By.XPATH,self.clk_IIndproduct_xpath)
        self.act.move_to_element(self.second).perform()

    def addcart2(self):
        self.addc1=self.driver.find_element(By.XPATH,self.clk_addcart1_xpath)
        self.act.move_to_element(self.addc1).click().perform()

    def viewcart(self):
        self.driver.find_element(By.XPATH,self.clk_viewcart_xpath).click()

    def blueTop(self):
        return self.driver.find_element(By.XPATH,self.chk_blueTop_xpath).text

    def mensTshirt(self):
        return self.driver.find_element(By.XPATH,self.chk_mensTshirt_xpath).text


    # def con(self):
    #      self.driver.find_element(By.XPATH,self.clk_continue_xpath).click()




