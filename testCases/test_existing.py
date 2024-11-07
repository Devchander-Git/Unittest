import os

from pageObjects.existingemail import existingEmail
from utilities import randomString
from utilities.readProperties import ReadConfig


class Test_Existingmail():
    baseURL=ReadConfig().getApplicationURL()

    def test_Existmail(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.em=existingEmail(self.driver)
        self.em.setsignlogin()
        self.name=randomString.random_string_generator()
        self.em.setname(self.name)
        # self.mail=randomString.random_string_generator()+"@gmail.com"
        self.em.setemail("fortune@gmail.com")
        self.em.clickLogin()

        self.msg=self.em.message()

        if self.msg == "Enter Account Information":
           assert True
           self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//test_login1.png")
            assert False
            self.driver.close()
