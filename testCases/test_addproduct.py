import os
import time

from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.addProduct import addProduct
from utilities.readProperties import ReadConfig


class Test_addingproduct():
    baseURL=ReadConfig().getApplicationURL()

    def test_cart(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)



        self.adp =addProduct(self.driver)

        self.adp.clickProduct()
        time.sleep(3)

        self.adp.firstProduct()
        time.sleep(3)
        self.adp.addcart1()
        time.sleep(3)
        self.adp.continuecart()
        self.adp.IIproduct()
        time.sleep(3)
        self.adp.addcart2()
        time.sleep(3)
        self.adp.continuecart()
        self.adp.viewcart()
        self.btop=self.adp.blueTop()
        self.mshirt=self.adp.mensTshirt()

        if self.btop == "Blue Top" and self.mshirt== "Men Tshirt":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//test_addproduct1.png")
            assert False


        time.sleep(3)




