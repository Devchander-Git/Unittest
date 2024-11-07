import os

from pageObjects.searchProduct import searchProduct
from utilities.readProperties import ReadConfig


class Test_search():
    baseURL=ReadConfig().getApplicationURL()

    def test_searchItem(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.si=searchProduct(self.driver)
        self.si.clickProduct()
        self.si.search("Fancy Green Top")
        self.confirm = self.si.clksearch()

        if self.confirm == "Fancy Green Top":
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//test_searchProduct.png")
            assert False



