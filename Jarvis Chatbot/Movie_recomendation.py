"""
Created on Mon Jun 29 23:31:57 2020

@author: aurouS_EeRiE
"""


from selenium import webdriver

class recom():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\\Users\\SRILEKHA\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
    def recom_info(self):
        self.driver.get(url = 'https://www.imdb.com/chart/moviemeter/?ref =nv_mv_mpm')
        select = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
        select.click()
        
# bot = recom()
# bot.recom_info()