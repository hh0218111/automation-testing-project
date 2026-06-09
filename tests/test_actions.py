import allure
from pages.actions_page import ActionsPage

@allure.feature("高级交互")
class TestActions:
    """WebDriverUniversity Actions 页面测试 — 拖拽/双击/按住/悬停"""

    @allure.story("拖拽操作")
    def test_drag_drop(self, actions_page):
        """测试：拖拽元素到目标区，验证文字变成 Dropped!"""
        result = actions_page.do_drag_drop()
        print(f"拖放后目标区文字：{result}")
        assert result == "Dropped!"

    @allure.story("双击操作")
    def test_dblclick(self, actions_page):
        """测试：双击按钮，验证 class 里多了 'double'"""
        result = actions_page.do_dblclick()
        print(f"双击后 class：{result}")
        assert "double" in result

    @allure.story("按住不放")
    def test_click_hold(self, actions_page):
        """测试：按住盒子 1.5 秒，验证文字改变"""
        result = actions_page.do_click_hold()
        print(f"按住后文字：{result}")
        assert "Well done" in result

    @allure.story("悬停下拉菜单")
    def test_hover(self, actions_page):
        """测试：悬停第一个按钮，验证下拉菜单链接出现"""
        result = actions_page.do_hover(btn_num=1)
        print(f"下拉链接文字：{result}")
        assert "Link" in result
