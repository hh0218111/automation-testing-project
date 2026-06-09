from playwright.sync_api import Page, expect


class LoginPortalPage:
    def __init__(self, page: Page):
        self.page = page
        # 元素定位
        self.username_input = page.locator("#text")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def goto(self):
        """打开登录页面"""
        self.page.goto("https://webdriveruniversity.com/Login-Portal/index.html")

    def login(self, user: str, pwd: str) -> str:
        """登录并返回弹窗文字"""
        result = {"msg": ""}

        def handle_dialog(dialog):
            result["msg"] = dialog.message
            dialog.accept()

        # ⚠️ 关键：page.once 在 click 之前注册，
        # 弹窗一出现就自动处理，不会阻塞 click
        self.page.once("dialog", handle_dialog)

        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_btn.click()

        # 给弹窗一点时间被处理
        self.page.wait_for_timeout(500)

        return result["msg"]

    def assert_success(self, msg: str):
        """断言登录成功"""
        assert "validation succeeded" in msg.lower(), f"期望成功，实际：{msg}"

    def assert_fail(self, msg: str):
        """断言登录失败"""
        assert "validation failed" in msg.lower(), f"期望失败，实际：{msg}"
