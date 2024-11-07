from selenium.webdriver.common.by import By


class searchProduct():
    lnk_product_xpath="//a[@href='/products']"
    txt_searchbox_xpath="//input[@id='search_product']"
    clk_searchbutton_xpath="//button[@id='submit_search']"


    def __init__(self,driver):
        self.driver=driver

    def clickProduct(self):
        self.driver.find_element(By.XPATH,self.lnk_product_xpath).click()

    def search(self,items):
        try:
            self.driver.find_element(By.XPATH,self.txt_searchbox_xpath).send_keys(items)
        except:
            None

    def clksearch(self):

        self.driver.find_element(By.XPATH,self.clk_searchbutton_xpath).click()