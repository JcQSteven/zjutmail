#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class BrowserTest:
    browser = None
    def getBrowser(self):
        self.browser = webdriver.Chrome()
        return self

    def getWeb(self,url):
        self.browser.get(url)

    def getElement(self,element):
        try:
            wait = WebDriverWait(self.browser, 5)
            ele = wait.until(lambda x: x.find_element_by_xpath(element))
        except:
            print("元素不存在")
            raise
        return ele

    def setElement(self,element,param):
        ele = self.getElement(element)
        ele.clear()
        ele.send_keys(param)

    def clickElement(self,element):
        ele = self.browser.find_element_by_xpath(element)
        ele.click()

    def close(self):
        self.browser.close()

class FileObj:
    route = None
    def setRoute(self,route):
        self.route = route

    def Write(self,str):
        with open(self.route,'a') as f:
            f.write(str+'\n')




setPswd = '123qweQWE'
Outputfile = FileObj()
Outputfile.setRoute("/Users/jerry-pc/Desktop/1.out")
browser = BrowserTest()

count = -1
for count, f in enumerate(open('/Users/jerry-pc/Desktop/1.in', 'rU')):
    user,pswd = f.strip('\n').split(",")
    print(user+"  "+pswd)

    browser.getBrowser().getWeb(url="http://mail.zjut.edu.cn/")
    browser.setElement('//input[@id="user"]',user)
    browser.setElement('//input[@id="password"]',pswd)
    browser.clickElement('//input[@id="submit"]')

    try:
        browser.setElement('//input[@id="oldpassword"]',"123") #实际使用时修改为pswd
        browser.setElement('//input[@id="newpassword"]',setPswd)
        browser.setElement('//input[@id="repassword"]',setPswd)
        browser.clickElement('//div[@class="layercontentbtn"]/input')
    except:
        Outputfile.Write("%s,%s,Error,%s"%(user,pswd,pswd))
    else:
         Outputfile.Write("%s,%s,Success,%s"%(user,pswd,setPswd))

    browser.close()
    count += 1


