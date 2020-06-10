from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DispalyPage(BaseAction):
    # 显示按钮
    dispaly_button = By.XPATH,"//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button = By.ID,"com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID,"android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        self.click_dispaly()
    # 显示
    def click_dispaly(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.find_element(self.dispaly_button).click()
        self.click(self.dispaly_button)
    #点击搜索按钮
    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)
    #输入文字
    def input_search_text(self,text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.find_element(self.input_text_view).send_keys("hello")
        self.input_text(self.input_text_view,text)
    # 返回
    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
