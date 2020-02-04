from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Bkd(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def web(self):
        self.driver.get('https://bkd.lldikti4.or.id/index.php')
        sleep(1)
        self.driver.find_element_by_name('NIDN').send_keys('0410118609')
        sleep(1)
        self.driver.find_element_by_name('Password').send_keys('11/10/1986')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/input').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[1]/div/a[3]/font/input').click()
        sleep(1)
        
        
        limit=2
        pintu=True
        while(pintu):
            try:
                self.driver.get('https://bkd.lldikti4.or.id/listtasemester.php')
                print('semester')
                print(self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/font[2]/table/tbody/tr['+str(limit)+']/td[2]/font').text)
                print('tahun')
                print(self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/font[2]/table/tbody/tr['+str(limit)+']/td[3]/font').text)
                self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/font[2]/table/tbody/tr['+str(limit)+']/td[4]/a/font/input').click()
                print('TTD Kajur/Prodi/Departemen')
                print(self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[2]/td[4]/font').text)
                print('TTD Asesor 1')
                print(self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[2]/td[5]/font').text)
                print('TTD Asesor 2')
                print(self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/table[1]/tbody/tr[2]/td[6]/font').text)
                print('======================================================================')
                limit+=1
            except:
                self.driver.quit()
                pintu=False
                

        