import os,sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):
    # 点击更多
    more_button = By.XPATH,"//*[contains(@text,'更多')]"
    # 移动网络
    network_button = By.XPATH,"//*[contains(@text,'移动网络')]"
    # 首选网络类型
    first_network_button = By.XPATH,"//*[contains(@text,'首选网络类型')]"
    # 移动网络2G
    network_2g = By.XPATH,"//*[contains(@text,'2G')]"
    # 移动网络3G
    network_3g = By.XPATH,"//*[contains(@text,'3G')]"

    # def __init__(self,driver):
    #     self.driver = driver
    # 点击更多
    def click_more(self):
        # self.find_element(self.more_button).click()
        self.click(self.more_button)
    # 移动网络
    def click_network(self):
        # self.find_element(self.network_button).click()
        self.click(self.network_button)
    # 首选网络类型
    def click_first_network(self):
        # self.find_element(self.first_network_button).click()
        self.click(self.first_network_button)
    # 移动网络2g
    def click_2g(self):
        # self.find_element(self.network_2g).click()
        self.click(self.network_2g)
    # 移动网络3g
    def click_3g(self):
        # self.find_element(self.network_3g).click()
        self.click(self.network_3g)
