from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class allProduct():
    clk_product_xpath="//a[@href='/products']"
    clk_firstproduct_xpath="//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]"
    text_confirm_xpath="//h2[normalize-space()='Blue Top']"

    def __init__(self,driver):
        self.driver=driver

    def setProduct(self):
        self.driver.find_element(By.XPATH,self.clk_product_xpath).click()

    def mousehover(self):
        self.act = self.ActionChains(self.driver)
        self.driver.find_element(By.XPATH, self.clk_firstproduct_xpath).click()

    def clkfirstProduct(self):





