import os.path
import time

from pageObjects.contactus import contactUs
from utilities.readProperties import ReadConfig


class Test_uploadFile():
    baseURL=ReadConfig().getApplicationURL()

    def test_upload(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.up=contactUs(self.driver)
        self.up.scrolldown()
        self.up.setcontact()
        self.up.setname("swarna")
        self.up.setemail("swarnambigai@gmail.com")
        self.up.setsubject("hi")
        self.up.msg("happy diwali")
        self.up.upload("C:/Users\dev_c\PycharmProjects/unittesting/screenshots/test_existing.png")
        self.up.submit()
        self.up.alertwindow()

        self.confmMsg=self.up.confMsg()
        if self.confmMsg == "Success! Your details have been submitted successfully.":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//test_upload.png")
            assert False
        self.up.clickHome()

time.sleep(10)