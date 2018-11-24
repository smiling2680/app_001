from Base.Base import Base
import Page,allure

class Person_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        
    @allure.step(title="获取我的收藏文本操作")
    def get_mylike_data(self):
        """获取我的收藏文本"""
        like_data = self.search_element(Page.my_like_id).text
        allure.attach("获取到的数据","{}".format(like_data))
        return like_data 
    
    @allure.step(title="点击设置按钮")
    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(Page.setting_btn_id)