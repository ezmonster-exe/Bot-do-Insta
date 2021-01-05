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
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('seu email')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('sua senha')
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
        
        while True:
            try:
                for i in range(1,6):
                    
                    xPath = '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[{}]/div[3]/button/div'

                    time.sleep(5)

                    nx = self.driver.find_element_by_xpath(xPath.format(str(i)))
                    nx.click()          
                break    
            except:
                # k2 = [item for item in self.driver.find_elements_by_class_name('aOOlW') if item.get_attribute('innerHTML') == 'OK'][0]
                # for item in self.driver.find_elements_by_class_name('aOOlW'):
                #     if item.get_attribute('innerHTML') == 'OK':
                #         item.click()
                
                time.sleep(1)
                k2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]')
                time.sleep(2)
                k2.click()    
                

    
    def likemenbers(self):
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,800)')
        h1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[1]/div[3]/section[1]/span[1]/button')
        h2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[2]/div[3]/section[1]/span[1]/button')
        h3 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[3]/div[3]/section[1]/span[1]/button')
        h4 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[4]/div[3]/section[1]/span[1]/button')
        h5 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[3]/div/article[5]/div[3]/section[1]/span[1]/button')
        time.sleep(1)

        while True:
            try:
                h1.click()
                self.driver.execute_script('window.scrollTo(0,800)')
                time.sleep(2)
                h2.click()
                self.driver.execute_script('window.scrollTo(0,1600)')
                time.sleep(5)
                h3.click()
                self.driver.execute_script('window.scrollTo(0,2400)')
                time.sleep(2)
                h4.click()
                self.driver.execute_script('window.scrollTo(0,3200)')
                time.sleep(5)
                h5.click
                self.driver.execute_script('window.scrollTo(0,4000)')
                self.driver.refresh()
                time.sleep(3)

                break
            except:
                time.sleep(1)
                k2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]')
                time.sleep(2)
                k2.click()
                  
    def perfil(self):

        while True:
            try:
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
                break
            except:
                time.sleep(2)
                k3 = [item for item in self.driver.find_elements_by_class_name('aOOlW') if item.get_attribute('innerHTML') == 'OK'][0]

                # for item in self.driver.find_elements_by_class_name('aOOlW'):
                #     if item.get_attribute('innerHTML') == 'OK':
                #         item.click()


  
p = Localizador()
p.loginAccounts()
p.InterfaceTwo()
p.varclickfollow()
p.likemenbers()
p.perfil()

del p

input('ok')
