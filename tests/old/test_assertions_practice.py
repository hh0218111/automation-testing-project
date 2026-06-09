""" 6种playwright断言练习 """

import pytest
from playwright.sync_api import Page,expect

Page_URL = "file:///D:/test_locator.html"   # ← 把 test_local 改成 test_locator


class TestAssertionsPractice:
    def test_01_visible(self,page:Page):
        #断言1，to_be_visible —— 元素是否可见

        page.goto(Page_URL)
        btn=page.locator("#login-btn")
        expect(btn).to_be_visible()

    def test_02_title(self,page:Page):
        #断言2，to_have_title() —— 页面标题是否正确

        page.goto(Page_URL)
        expect(page).to_have_title("元素定位练习场")
    
    def test_03_text(self, page: Page):
        """断言3：to_have_text — 文字完全匹配"""
        page.goto(Page_URL)
        # 点击登录按钮后，结果区显示什么？（在HTML里找 onclick 事件）
        page.locator("#login-btn").click()
        result = page.locator("#button-result")
        expect(result).to_have_text("✅ 登录按钮被点击了")


    # def test_04_contain_text(self,page:Page):
    #     """断言4：to_contain_text —— 包含某段文字"""

    #     page.goto(Page_URL)
    #     expect(page.locator("body")).to_contain_text("运d动")

    def test_05_value(self, page: Page):
        """断言5：to_have_value — 输入框里的值"""
        page.goto(Page_URL)
        username=page.locator("#username")
        username.fill("张三")
        expect(username).to_have_value("张三")

    def test_06_url(self,page:Page):
        """ 断言6：to_have_url —— 页面url"""

        page.goto(Page_URL)
        import re
        expect(page).to_have_url(re.compile(r"file:///D:"))
    