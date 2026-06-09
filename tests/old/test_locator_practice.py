"""
元素定位练习 —— 从零开始
========================
页面：data/locator_practice.html（8个区域，各种元素都有）

每道题你只需要填 page.locator(???) 里的选择器。
运行命令：
    cd D:\Claude code\自动化测试项目
    pytest tests/test_locator_practice.py -v -s
"""

import pytest
from playwright.sync_api import Page, expect

PAGE_URL = "file:///D:/Claude code/自动化测试项目/data/locator_practice.html"


class TestLocatorID:
    """第1关：通过 id 定位 —— 最常用"""

    def test_find_username_by_id(self, page: Page):
        """
        练习1：找到"用户名"输入框（看 HTML：id="username"）
        规则：id 定位用 #号，写成 "#username"
        """
        page.goto(PAGE_URL)
        box = page.locator("#username")      # ← 把 ___ 换成 #username
        box.fill("张三")
        assert box.input_value() == "张三"

    def test_find_login_btn_by_id(self, page: Page):
        """
        练习2：找到"登录"按钮（HTML：id="login-btn"）
        """
        page.goto(PAGE_URL)
        btn = page.locator("#login-btn")      # ← 换成 #login-btn
        expect(btn).to_be_visible() 
        btn.click()
        expect(page.locator("#button-result")).to_contain_text("登录按钮被点击了")


class TestLocatorClass:
    """第2关：通过 class 定位 —— 同时定位多个同类元素"""

    def test_find_search_box_by_class(self, page: Page):
        """
        练习3：找到搜索框（HTML：class="search-box"）
        规则：class 定位用 .号，写成 ".search-box"
        """
        page.goto(PAGE_URL)
        box = page.locator(".search-box")      # ← 换成 .search-box
        box.fill("Playwright")
        assert box.input_value() == "Playwright"

    def test_count_cards_by_class(self, page: Page):
        """
        练习4：统计卡片数量（HTML：class="card" 有 3 个）
        """
        page.goto(PAGE_URL)
        cards = page.locator(".card")    # ← 换成 .card
        assert cards.count() == 4


class TestLocatorText:
    """第3关：通过文字定位 —— 找"包含某文字"的元素"""

    def test_find_button_by_text(self, page: Page):
        """
        练习5：找到"取消"按钮（页面上唯一写着"取消"的按钮）
        规则：用 has_text 或 text=...
        两种写法等价：
            page.locator("button:has-text('取消')")
            page.get_by_text("取消")

        提示：get_by_text 是 Playwright 专门用来按文字定位的方法，比 has-text 更推荐。
        """
        page.goto(PAGE_URL)
        btn = page.get_by_text("取消")   # ← 换成 取消
        btn.click()

    def test_find_link_by_text(self, page: Page):
        """
        练习6：找到"百度一下"链接
        """
        page.goto(PAGE_URL)
        link = page.get_by_text("百度一下")  # ← 换成 百度一下
        href = link.get_attribute("href")
        assert "baidu.com" in href


class TestLocatorAttribute:
    """第4关：通过属性定位 —— 更精准的找法"""

    def test_find_by_placeholder(self, page: Page):
        """
        练习7：找到 placeholder="请输入用户名" 的输入框
        规则：[属性名="属性值"]
        """
        page.goto(PAGE_URL)
        box = page.locator('[placeholder="请输入用户名"]')  # ← 换成 请输入用户名
        box.fill("test")
        assert box.input_value() == "test"

    def test_find_by_data_attribute(self, page: Page):
        """
        练习8：找到 data-role="contact" 的邮箱输入框
        自定义属性 data-xxx 也可以用 [属性名="值"] 来定位
        """
        page.goto(PAGE_URL)
        box = page.locator('[data-role="contact"]')  # ← 换成 data-role
        assert box.get_attribute("type") == "email"

    def test_find_by_name_attribute(self, page: Page):
        """
        练习9：找到 name="user" 的输入框
        """
        page.goto(PAGE_URL)
        box = page.locator('[name="user"]')  # ← 换成 user
        box.fill("hello")
        assert box.input_value() == "hello"


class TestLocatorNesting:
    """第5关：嵌套定位 —— 先找到大区域，再在里面找小元素"""

    def test_find_score_in_table(self, page: Page):
        """
        练习10：表格里找到"张三"的分数（95）
        思路：
            1. 先定位到表格的行（tr），用 :has-text 找到包含"张三"的那行
            2. 再在这行里找 class="score" 的单元格
        写成：page.locator("tr:has-text('张三') .score")
        """
        page.goto(PAGE_URL)
        cell = page.locator("tr:has-text('张三') .score")   # ← 换成 tr:has-text('张三') .score
        assert cell.inner_text() == "95"

    def test_find_card_by_data_id(self, page: Page):
        """
        练习11：找到第2张卡片（data-id="2" 的那张）
        """
        page.goto(PAGE_URL)
        card = page.locator('[data-id="2"]')  # ← 换成 2
        assert "明天交实验报告" in card.inner_text()


class TestLocatorFormElements:
    """第6关：表单元素 —— 下拉框、复选框、单选框"""

    def test_select_city(self, page: Page):
        """
        练习12：在下拉框里选"深圳"
        规则：page.select_option() 用 value 值
        HTML 里：<option value="shenzhen">深圳</option>
        """
        page.goto(PAGE_URL)
        dropdown = page.locator("#city")    # ← 换成 city
        dropdown.select_option("shenzhen")      # ← 换成 shenzhen
        assert dropdown.input_value() == "shenzhen"

    def test_check_hobby(self, page: Page):
        """
        练习13：勾选"游戏"复选框
        规则：找到复选框元素，调用 .check()
        HTML：<input type="checkbox" id="hobby-game" ...>
        """
        page.goto(PAGE_URL)
        checkbox = page.locator("#hobby-game")    # ← 换成 hobby-game
        checkbox.check()
        assert checkbox.is_checked()

    def test_select_gender(self, page: Page):
        """
        练习14：选择性别"男"
        规则：单选按钮用 .check()
        """
        page.goto(PAGE_URL)
        radio = page.locator("#gender-male")       # ← 换成 gender-male
        radio.check()
        assert radio.is_checked()


class TestLocatorDynamic:
    """第7关：动态元素 —— 隐藏/显示的元素怎么处理"""

    def test_toggle_hidden_message(self, page: Page):
        """
        练习15：点击按钮让隐藏消息显示
        先断言消息隐藏 → 点击按钮 → 断言消息可见
        """
        page.goto(PAGE_URL)

        msg = page.locator("#dynamic-msg")
        # 初始状态：消息是隐藏的
        expect(msg).not_to_be_visible()

        # 点击按钮显示消息
        page.locator("#show-msg-btn").click()   # ← 换成 show-msg-btn

        # 现在消息应该可见了
        expect(msg).to_be_visible()


# ========================================
#  答案参考（做完再看！）
# ========================================
#  练习1: "#username"
#  练习2: "#login-btn"
#  练习3: ".search-box"
#  练习4: ".card"
#  练习5: "取消"
#  练习6: "百度一下"
#  练习7: "请输入用户名"
#  练习8: "data-role"
#  练习9: "user"
#  练习10: "tr:has-text('张三') .score"
#  练习11: "2"
#  练习12: "city" / "shenzhen"
#  练习13: "hobby-game"
#  练习14: "gender-male"
#  练习15: "show-msg-btn"
