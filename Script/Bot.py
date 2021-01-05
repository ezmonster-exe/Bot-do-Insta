from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Localizador:
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.maximize_window()
        self.urlogin = 'https://www.instagram.com'
            
    def loginAccounts(self):
        self.driver.get(self.urlogin)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('lucasoleoncio807@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('allox2020')
        time.sleep(1)
        n1 = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        n1.click()

    def InterfaceTwo(self):
        time.sleep(5)
        n2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        n2.click()
        time.sleep(3)
        n3 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        n3.click()
    
    def comits(self):
        
        time.sleep(4)
        self.driver.execute_script('scrollTo(0,400)')
        time.sleep(8)
        v1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[1]/div[3]/section[1]/span[2]/button')
        time.sleep(6)
        v1.click()
        time.sleep(3)
        v2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button')
        v2.click()
        v3 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        time.sleep(2)
        v3.send_keys('Uau')
        v4 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
        time.sleep(6)
        v4.click()
        time.sleep(12)

    def status(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(10)
        g1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[3]/div/button/div[2]')
        time.sleep(3)
        g1.click()
        time.sleep(600)
        # time.sleep(1200)
    
    def varclickfollow(self):

        self.driver.get('https://www.instagram.com/')
        while True:
            try:
                for i in range(1,6):
                    
                    xPath = '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[{}]/div[3]/button/div'

                    time.sleep(5)

                    nx = self.driver.find_element_by_xpath(xPath.format(str(i)))
                    nx.click()          
                break    
            except:
                time.sleep(1)
                k2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]')
                time.sleep(2)
                k2.click()    
                

    
    def likemenbers(self):
        time.sleep(5)
        self.driver.execute_script('window.scrollTo(0,800)')
        time.sleep(2)
        h1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[1]/div[3]/section[1]/span[1]/button')
        h2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[2]/div[3]/section[1]/span[1]/button')
        h3 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[3]/div[3]/section[1]/span[1]/button')
        h4 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[4]/div[3]/section[1]/span[1]/button')
        time.sleep(1)

        while True:
            try:
                h1.click()
                time.sleep(3)
                self.driver.execute_script('window.scrollTo(0,1800)')
                h2.click()
                self.driver.execute_script('window.scrollTo(0,2800)')
                time.sleep(8)
                h3.click()
                self.driver.execute_script('window.scrollTo(0,3800)')
                time.sleep(3)
                h4.click()
                self.driver.execute_script('window.scrollTo(0,4000)')
                time.sleep(8)
                self.driver.refresh()
                time.sleep(3)

                break
            except:
                time.sleep(1)
                k2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]')
                time.sleep(2)
                k2.click()
                  
    def clickperf(self):
        time.sleep(6)
        self.driver.get('https://www.instagram.com/')
        t1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
        time.sleep(3)
        t1.click()
        t2 = self.driver.find_element_by_xpath('//*[@id="f149c22a8be0a14"]/div/div/div')
        time.sleep(2)
        t2.click()
    
    def unfollow(self):
        

















        
                # time.sleep(2)
                # k4 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button[2]')
                # time.sleep(2)
                # k4.click()
                # time.sleep(5)


p = Localizador()
p.loginAccounts()
p.InterfaceTwo()
p.comits()
p.status()
p.varclickfollow()
p.likemenbers()
while True:
    p.clickperf()

del p