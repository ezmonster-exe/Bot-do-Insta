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
        time.sleep(1)
        n3 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        n3.click()

    def varclickfollow(self):
        
        for i in range(1,6):
            
            xPath = '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[{}]/div[3]/button/div'

            time.sleep(5)

            nx = self.driver.find_element_by_xpath(xPath.format(str(i)))
            nx.click()

            self.driver.refresh()
            
           
        time.sleep(5)
       
    #==========================PROCESSO DE UNFOLOW==========================#

    def perfil(self):

       perfil = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
       perfil.click()


       time.sleep(3)

       abrir = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div')
       abrir.click()

       time.sleep(5)

       seguindo = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
       seguindo.click()

       time.sleep(2)

       unfollow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button')
       unfollow.click()

       time.sleep(5)

       certo = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
       certo.click()

       time.sleep(2)

       unfollow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[2]/div/div[3]/button')
       unfollow.click()

       time.sleep(5)

       certo = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
       certo.click()

       time.sleep(2)

       unfollow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[3]/div/div[3]/button')
       unfollow.click()

       time.sleep(5)

       certo = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
       certo.click()

       time.sleep(2)

       unfollow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[4]/div/div[3]/button')
       unfollow.click()

       time.sleep(5)

       certo = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
       certo.click()

       time.sleep(2)

       unfollow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[5]/div/div[3]/button')
       unfollow.click()

       time.sleep(5)

       certo = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
       certo.click()

       time.sleep(2)

       unfollow = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[6]/div/div[3]/button')
       unfollow.click()

       time.sleep(5)

       certo = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
       certo.click()
       time.sleep(2)
       self.driver.refresh()

   
p = Localizador()
p.loginAccounts()
p.InterfaceTwo()
p.varclickfollow()
while True:
    p.perfil()

del p

input('ok')