from selenium.webdriver.common.by import By


class contactUs():
    btn_contactus_xpath="//a[normalize-space()='Contact us']"
    txt_name_xpath="//input[@placeholder='Name']"
    txt_mail_xpath="//input[@placeholder='Email']"
    txt_subject_xpath="//input[@placeholder='Subject']"
    txt_msg_xpath="//textarea[@id='message']"
    file_upload_xpath="//input[@name='upload_file']"
    click_submit_xpath="//input[@name='submit']"
    txt_confmmsg_xpath="//div[@class='status alert alert-success']"
    btn_home_xpath="//span[normalize-space()='Home']"

    def __init__(self,driver):
        self.driver=driver


    def scrolldown(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.value = self.driver.execute_script("return window.pageYOffset;")

    def setcontact(self):
        self.driver.find_element(By.XPATH,self.btn_contactus_xpath).click()

    def setname(self,name):
        self.driver.find_element(By.XPATH,self.txt_name_xpath).send_keys(name)

    def setemail(self,mail):
        self.driver.find_element(By.XPATH,self.txt_mail_xpath).send_keys(mail)

    def setsubject(self,sub):
        self.driver.find_element(By.XPATH,self.txt_subject_xpath).send_keys(sub)

    def msg(self,msg):
        self.driver.find_element(By.XPATH,self.txt_msg_xpath).send_keys(msg)

    def upload(self,file):
        self.driver.find_element(By.XPATH,self.file_upload_xpath).send_keys(file)

    def submit(self):
        self.driver.find_element(By.XPATH,self.click_submit_xpath).click()

    def alertwindow(self):
        self.driver.switch_to.alert.accept()

    def confMsg(self):
        return self.driver.find_element(By.XPATH,self.txt_confmmsg_xpath).text



    def clickHome(self):
        self.driver.find_element(By.XPATH,self.btn_home_xpath).click()