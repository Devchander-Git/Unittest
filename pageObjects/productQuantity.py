

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class quantityPage():
    clk_product_xpath="//a[@href='/products']"
    clk_viewproduct_xpath="//div[4]//div[1]//div[2]//ul[1]//li[1]//a[1]//i[1]"
    add_increase_xpath="//input[@id='quantity']"
    clk_addtocart_xpath="//button[@type='button']"
    button_viewtocart_xpath="//u[normalize-space()='View Cart']"
    clk_confmsg_xpath="//p[@class='cart_total_price']"


    def __init__(self,driver):
        self.driver=driver



    def product(self):
        self.driver.find_element(By.XPATH,self.clk_product_xpath).click()

    def viewcart(self):
        self.driver.find_element(By.XPATH,self.clk_viewproduct_xpath).click()



    def increasecart(self,num):

        self.quan=self.driver.find_element(By.XPATH,self.add_increase_xpath)
        self.quan.clear()
        self.quan.send_keys(num)

    def addtocart(self):
        self.driver.find_element(By.XPATH,self.clk_addtocart_xpath).click()

    def viewtocart(self):
        self.driver.find_element(By.XPATH,self.button_viewtocart_xpath).click()

    def confmsg(self):

        return self.driver.find_element(By.XPATH,self.clk_confmsg_xpath).text






