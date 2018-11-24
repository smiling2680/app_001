from Base.Base import Base
import Page,allure


class Home_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        
    @allure.step(title="点击首页我的")
    def click_my_btn(self):
        """点击首页我按钮"""
        self.click_element(Page.my_btn_id)