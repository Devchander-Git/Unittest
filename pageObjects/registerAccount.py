from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class registerAccount():
    clk_Mr_xpath = "//label[@for='id_gender1']"
    clk_Mrs_xpath = "//label[@for='id_gender2']"
    txt_passWord_xpath = "//input[@id='password']"
    drop_dobDay_xpath = "//select[@id='days']"
    drop_dobMonth_xpath = "//select[@id='months']"
    drop_dobYear_xpath = "//select[@id='years']"
    chkbox_newspaper_xpath = "//input[@id='newsletter']"
    chkbox_specialoffer_xpath = "//input[@id='optin']"
    txt_firstname_xpath = "//input[@id='first_name']"
    txt_lastname_xpath = "//input[@id='last_name']"
    txt_companyname_xpath = "//input[@id='company']"
    txt_address1_xpath = "//input[@id='address1']"
    txt_address2_xpath = "//input[@id='address2']"
    drop_country_xpath = "//select[@id='country']"
    txt_state_xpath = "//input[@id='state']"
    txt_city_xpath = "//input[@id='city']"
    txt_pincode_xpath = "//input[@id='zipcode']"
    txt_mobile_xpath = "//input[@id='mobile_number']"
    click_createAcc_xpath = "//button[normalize-space()='Create Account']"
    clk_continue_xpath="//a[@class='btn btn-primary']"
    txt_display_xpath="//li[10]//a[1]"
    btn_delete_xpath="//a[normalize-space()='Delete Account']"
    btn_nextContinue_xpath="//a[@class='btn btn-primary']"


    def __init__(self,driver):
        self.driver=driver
    def scrolldown(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.value = self.driver.execute_script("return window.pageYOffset;")
    def setmr(self):
        self.driver.find_element(By.XPATH,self.clk_Mr_xpath).click()

    def setMrs(self):
        self.driver.find_element(By.XPATH,self.clk_Mrs_xpath)

    def setpassWord(self,pass1):
        self.driver.find_element(By.XPATH,self.txt_passWord_xpath).send_keys(pass1)

    def setdobDay(self,day):
        self.day=Select(self.driver.find_element(By.XPATH,self.drop_dobDay_xpath))
        self.day.select_by_visible_text(day)

    def setdobMonth(self,month):
        self.month=Select(self.driver.find_element(By.XPATH,self.drop_dobMonth_xpath))
        self.month.select_by_visible_text(month)

    def setdobYear(self,year):
        self.year=Select(self.driver.find_element(By.XPATH,self.drop_dobYear_xpath))
        self.year.select_by_visible_text(year)

    def setNewspaper(self):
       self.news=self.driver.find_element(By.XPATH,self.chkbox_newspaper_xpath)
       self.news.click()

    def setSpecialoffer(self):
        self.special=self.driver.find_element(By.XPATH,self.chkbox_specialoffer_xpath)
        self.special.click()


    def setFirstName(self,Fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(Fname)

    def setLastName(self,Lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(Lname)

    def setcompany(self,company):
        self.driver.find_element(By.XPATH,self.txt_companyname_xpath).send_keys(company)

    def setaddress1(self,add1):
        self.driver.find_element(By.XPATH,self.txt_address1_xpath).send_keys(add1)

    def setaddress2(self,add2):
        self.driver.find_element(By.XPATH,self.txt_address2_xpath).send_keys(add2)

    def setcountry(self,country):
        self.country=Select(self.driver.find_element(By.XPATH,self.drop_country_xpath))
        self.country.select_by_visible_text(country)

    def setstate(self,state):
        self.driver.find_element(By.XPATH,self.txt_state_xpath).send_keys(state)

    def setcity(self,city):
        self.driver.find_element(By.XPATH,self.txt_city_xpath).send_keys(city)

    def setpin(self,pin):
        self.driver.find_element(By.XPATH,self.txt_pincode_xpath).send_keys(pin)

    def setmobile(self,mbl):
        self.driver.find_element(By.XPATH,self.txt_mobile_xpath).send_keys(mbl)

    def clickAcc(self):
        self.driver.find_element(By.XPATH,self.click_createAcc_xpath).click()

    def btnContinue(self):
        self.driver.find_element(By.XPATH,self.clk_continue_xpath).click()

    def textloggedin(self):
        try:
            self.driver.find_element(By.XPATH,self.txt_display_xpath).is_dispalyed()
        except:
            None

    def btndelete(self):
        self.driver.find_element(By.XPATH,self.btn_delete_xpath).click()

    def nextContinue(self):
        self.driver.find_element(By.XPATH,self.btn_nextContinue_xpath).click()
