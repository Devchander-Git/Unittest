import os.path
import time

from pageObjects.productQuantity import quantityPage
from utilities.readProperties import ReadConfig


class Test_quantincreace():
    baseURL=ReadConfig().getApplicationURL()

    def test_quantity(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.qi=quantityPage(self.driver)
        self.qi.product()
        time.sleep(3)
        self.qi.viewcart()
        time.sleep(3)
        self.qi.increasecart("4")
        time.sleep(2)
        self.qi.addtocart()
        self.qi.viewtocart()
        self.msg=self.qi.confmsg()
        if self.msg== "Rs. 4000":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//test_increase.png")
            assert False


        time.sleep(10)


