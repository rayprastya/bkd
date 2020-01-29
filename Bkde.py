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