import os.path

from pageObjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig


class Test_loginAccount():
    baseURL=ReadConfig().getApplicationURL()

    def test_loginAcc(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.la=loginPage(self.driver)
        self.la.signlogin()
        self.la.setemail("fortune@gmail.com")
        self.la.setpass("asumathi_4u")
        self.la.clickLogin()
        self.msg=self.la.massage()
        #
        if self.msg =="Delete Account":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//test_login1.png")
            assert False
            self.driver.close()

        self.la.clicklogout()