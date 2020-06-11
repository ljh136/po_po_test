import os,sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.dispaly_page import DispalyPage

class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.dispaly_page = DispalyPage(self.driver)

    def test_mobile_display_input(self):
        # 点击放大镜
        self.dispaly_page.click_search()
        # 输入文字
        self.dispaly_page.input_search_text("123")
        # 点击返回
        self.dispaly_page.click_back()
#1
#2
#3
