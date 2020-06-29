"""
Created on Mon Jun 29 23:32:33 2020

@author: aurouS_EeRiE
"""


from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\\Users\\SRILEKHA\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
    def play(self, name):
        self.name = name
        self.driver.get(url = 'https://www.youtube.com/results?search_query='+name)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]')
        video.click()
        
# bot = music()
# bot.play("ala vaikunta puramlo")