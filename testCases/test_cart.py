from pageObjects.cartPage import cartPage
from utilities.readProperties import ReadConfig


class Test_Cart():
    baseURL=ReadConfig().getApplicationURL()

    def test_cartsub(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.cb=cartPage(self.driver)
        self.cb.clkcart()
        self.cb.setmail("dev")
        self.cb.clkarrow()