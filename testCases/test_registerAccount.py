import os.path
import time

from pageObjects.registerAccount import registerAccount
from pageObjects.registerUser import registerUser
from utilities import randomString
from utilities.readProperties import ReadConfig


class Test_registerAccount():
    baseURL=ReadConfig().getApplicationURL()


    def test_registerAccount(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.ru=registerUser(self.driver)
        self.ru.setSignup()
        self.userName=randomString.random_string_generator()
        self.ru.setNewUser(self.userName)
        self.emailId=randomString.random_string_generator()+"@gmail.com"
        self.ru.setEmail(self.emailId)
        self.ru.submit()


        self.ra=registerAccount(self.driver)
        self.ra.scrolldown()
        self.ra.setmr()
        self.ra.setpassWord("ashwanth")
        self.ra.setdobDay("6")
        self.ra.setdobMonth("October")
        self.ra.setdobYear("2016")
        self.ra.setNewspaper()
        self.ra.setSpecialoffer()
        self.ra.setFirstName("Ashmita")
        self.ra.setLastName("Dev")
        self.ra.setcompany("Lova")
        self.ra.scrolldown()
        self.ra.setaddress1("28,near police colony")
        self.ra.setaddress2("mannachanallur")
        self.ra.setcountry("India")
        self.ra.setstate("Karnataka")
        self.ra.setcity("bangalore")
        self.ra.setpin("621005")
        self.ra.setmobile("7795644495")
        self.ra.clickAcc()
        self.ra.btnContinue()
        self.ra.textloggedin()
        self.ra.btndelete()
        self.ra.nextContinue()

time.sleep(10)
