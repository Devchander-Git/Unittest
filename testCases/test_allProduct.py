from pageObjects.allProduct import allProduct
from utilities.readProperties import ReadConfig


class Test_product():
    baseURL=ReadConfig().getApplicationURL()

    def test_allproduct(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.ap=allProduct(self.driver)
        self.ap.setProduct()
        self.ap.clkfirstProduct()




