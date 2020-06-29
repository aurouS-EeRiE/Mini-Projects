"""
Created on Mon Jun 29 23:32:15 2020

@author: aurouS_EeRiE
"""


from selenium import webdriver

class Movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\\Users\\SRILEKHA\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
    def movie_review(self, name):
        self.driver.get(url = 'https://www.google.com')
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + " movie reviews")
        submit = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        submit.click()
        
# bot = Movie()
# bot.movie_review("Titanic")