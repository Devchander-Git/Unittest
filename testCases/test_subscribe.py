import time

from pageObjects.subscribtion import subscribtion
from utilities.readProperties import ReadConfig


class Test_subscribe():
    baseURL=ReadConfig().getApplicationURL()

    def test_usersubscribe(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.us=subscribtion(self.driver)
        self.us.scrolldown()
        self.us.setmailId("swarna@gmail.com")
        self.us.clkarrow()


time.sleep(10)
