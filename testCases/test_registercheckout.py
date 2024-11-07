import os.path
import time

from pageObjects.registercheckout import registerCheckout
from utilities.readProperties import ReadConfig


class Test_regCheck():
    baseURL=ReadConfig().getApplicationURL()



    def test_regCheckout(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.rc=registerCheckout(self.driver)
        self.rc.signIn()
        self.rc.userEmail("woodland@gmail.com")
        self.rc.password("woodland_4u")
        self.rc.login()

        self.rc.clkproduct()
        time.sleep(2)
        self.rc.product1()
        time.sleep(3)
        self.rc.prdtCart1()
        time.sleep(3)
        self.rc.clkcontinue()
        self.rc.product2()
        time.sleep(3)
        self.rc.product2cart()
        time.sleep(3)
        self.check=self.rc.verification()
        if self.check=="Added!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots/test_checkout.png")
            self.driver.close()
            assert False
        self.rc.viewcart()


