import os,sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import NetworkPage

class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.networkPage = NetworkPage(self.driver)

    def test_mobile_network_2g(self):
        # 更多
        self.networkPage.click_more()
        # 移动网络
        self.networkPage.click_network()
        # 首选网络类型
        self.networkPage.click_first_network()
        # 移动网络2g
        self.networkPage.click_2g()

    def test_mobile_network_3g(self):
        self.networkPage.click_more()
        self.networkPage.click_network()
        self.networkPage.click_first_network()
        self.networkPage.click_3g()
        
    def test_mobile_network_4g(self):
        self.networkPage.click_more()
        self.networkPage.click_network()
        self.networkPage.click_first_network()
        self.networkPage.click_3g()
