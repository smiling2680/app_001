from Base.Base import Base
import Page,allure

class Login_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)
        
    @allure.step(title="登录")
    def login(self, username, password):
        """登录"""
        # 输入用户名
        allure.attach("输入用户名","{}".format(username))
        self.send_element(Page.login_name_id, username)
        # 输入密码
        allure.attach("输入密码","{}".format(password))
        self.send_element(Page.login_passwd_id, password)
        # 点击登录按钮
        allure.attach("点击登录按钮","点击")
        self.click_element(Page.login_btn_id)
        
    @allure.step(title="关闭登录页面")
    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(Page.login_close_btn_id)
        
    @allure.step(title="登录按钮状态")
    def if_login_btn(self):
        # 登录按钮是否存在， 存在返回True 不存在返回False
        try:
            allure.attach("登录按钮","存在")
            self.search_element(Page.login_btn_id)
            return True
        except:
            allure.attach("登录按钮","不存在")
            return False
