import os
import time

from pageObjects.newuserddt import newuserDDT
from utilities import XLUtils
from utilities.readProperties import ReadConfig


class Test_newuser():
    baseURL=ReadConfig().getApplicationURL()

    path=os.path.abspath(os.curdir)+"//testData/automationDDT.xlsx"

    def test_newuser(self,setup):
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status=[]

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.nuDDT=newuserDDT(self.driver)
        self.nuDDT.signup()


        for r in range(2,self.rows + 1):

          self.uemail=XLUtils.readData(self.path,'Sheet1',r,1)
          self.upwd = XLUtils.readData(self.path, 'Sheet1', r, 2)
          self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

          self.nuDDT.usremail(self.uemail)
          self.nuDDT.userpass(self.upwd)
          self.nuDDT.submit()
          time.sleep(3)
          self.target=self.nuDDT.istargetpagediplayed()

          if self.exp == 'Valid':
          #     if self.target == True:
          #         lst_status.append('Pass')
               self.nuDDT.logOut()
          #     else:
          #         lst_status.append('Fail')
          # elif self.exp == 'Invalid':
          #     if self.target == True:
          #         lst_status.append('Pass')
          #         self.nuDDT.logOut()
          #     else:
          #         lst_status.append('Pass')
          # self.driver.close()
          # # final validation
          # if "Fail" not in lst_status:
          #     assert True
          # else:
          #     assert False