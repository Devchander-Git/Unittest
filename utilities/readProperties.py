import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"//configuration/config.ini")

class ReadConfig():
    def getApplicationURL(self):
        url=config.get('commonInfo','baseURL')
        return url

    def getnewuser(self):
        newuser=config.get('commonInfo','newuser')
        return newuser

    def getemail(self):
        email=config.get('commonInfo','emailid')
