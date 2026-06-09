from playwright.sync_api import Page,expect

class LoginPage:
    """登录页面类 -  POM 示例"""

    def __init__(self,page:Page):
        self.page=page

        #定位器集中管理（__init__里只写定位器）
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login-btn")
        self.result_area = page.locator("#button-result")

    def goto(self):
        """ 打开登录页面 """
        self.page.goto("file:///D:/test_locator.html")

    def login(self,username:str,password: str):
        """ 执行登录操作"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()


    def assert_login_clicked(self):
        """断言登录按钮被点击"""
        expect(self.result_area).to_have_text("✅ 登录按钮被点击了")


