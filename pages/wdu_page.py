"""WebDriverUniversity 练习页面"""
from playwright.sync_api import Page, expect


class WDUDropdownPage:
    """下拉框/复选框/单选按钮练习页"""
    
    def __init__(self, page: Page):
        self.page = page
        # 下拉框
        self.dropdown1 = page.locator("#dropdowm-menu-1")
        self.dropdown2 = page.locator("#dropdowm-menu-2")
        self.dropdown3 = page.locator("#dropdowm-menu-3")
        # 复选框
        self.checkbox1 = page.locator("input[value='option-1']")
        self.checkbox2 = page.locator("input[value='option-2']")
        self.checkbox3 = page.locator("input[value='option-3']")
        self.checkbox4 = page.locator("input[value='option-4']")
        # 单选按钮
        self.radio_green = page.locator("input[value='green']")
        self.radio_blue = page.locator("input[value='blue']")
    
    def goto(self):
        self.page.goto("http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
    
    def select_language(self, value: str):
        """选编程语言"""
        self.dropdown1.select_option(value)
    
    def check_option(self, num: int):
        """勾选第 num 个选项 (1-4)"""
        getattr(self, f"checkbox{num}").check()
    
    def uncheck_option(self, num: int):
        getattr(self, f"checkbox{num}").uncheck()
    
    def select_color(self, color: str):
        """选颜色 (green/blue)"""
        getattr(self, f"radio_{color}").check()
