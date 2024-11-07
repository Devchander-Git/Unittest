import os

from pageObjects.registerUser import registerUser


class Test_register():
    baseURL="https://automationexercise.com/login"

    def test_register(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        self.ru=registerUser(self.driver)

        self.ru.setSignup()
        self.ru.setNewUser("ashmita")
        self.ru.setEmail("ashita@gmail.com")
        self.ru.submit()
        # self.conf_msg = self.ru.confirm_text()
        # self.driver.close()
        # if self.conf_msg == "Enter Account Information":
        #     assert True
        # else:
        #     assert False



