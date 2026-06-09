from playwright.sync_api import Page


class ActionsPage:
    """这段代码在整个项目中作用：WebDriverUniversity Actions 页面对象 — 封装拖拽/双击/按住/悬停 4 种操作"""

    def __init__(self, page: Page):
        self.page = page

        # ====== 1. 拖拽元素 ======
        # 可拖拽的盒子（初始文字 "DRAG ME TO MY TARGET!"）
        self.draggable = page.locator("#draggable")
        # 拖拽目标区（初始文字 "DROP HERE!"，拖入后变 "Dropped!"）
        self.droppable = page.locator("#droppable")

        # ====== 2. 双击元素 ======
        # 双点后 class 会从 "div-double-click" 变成 "div-double-click double"
        self.dblclick_btn = page.locator("#double-click")

        # ====== 3. 按住不放元素 ======
        # 按住后文字变 "Well done! keep holding that click now....."
        self.click_box = page.locator("#click-box")

        # ====== 4. 悬停按钮（hover 显示下拉菜单） ======
        self.hover_btn1 = page.get_by_text("Hover Over Me First!")
        self.hover_btn2 = page.get_by_text("Hover Over Me Second!")
        self.hover_btn3 = page.get_by_text("Hover Over Me Third!")

    def goto(self):
        """打开 Actions 页面"""
        self.page.goto("https://webdriveruniversity.com/Actions/index.html")

    # ====== 拖拽操作 ======
    def do_drag_drop(self) -> str:
        """这段代码的作用：把 draggable 拖到 droppable 上，返回拖放后的目标区文字"""
        self.draggable.drag_to(self.droppable)
        self.page.wait_for_timeout(300)
        return self.droppable.inner_text()

    # ====== 双击操作 ======
    def do_dblclick(self) -> str:
        """这段代码的作用：双击按钮，返回双击后的 class 属性（用于断言是否包含 'double'）"""
        self.dblclick_btn.dblclick()
        self.page.wait_for_timeout(300)
        return self.dblclick_btn.get_attribute("class")

    # ====== 按住操作 ======
    def do_click_hold(self) -> str:
        """这段代码的作用：鼠标按住 #click-box 不放，1 秒后读取文字并松开"""
        box = self.click_box.bounding_box()
        # 鼠标移到盒子中心，按下左键不放
        self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        self.page.mouse.down()
        self.page.wait_for_timeout(1500)  # 按住 1.5 秒
        text = self.click_box.inner_text()
        self.page.mouse.up()
        return text

    # ====== 悬停操作 ======
    def do_hover(self, btn_num: int) -> str:
        """这段代码的作用：悬停到第 N 个按钮上，返回出现的下拉菜单链接文字"""
        btn_map = {1: self.hover_btn1, 2: self.hover_btn2, 3: self.hover_btn3}
        btn = btn_map.get(btn_num)
        if btn is None:
            raise ValueError(f"btn_num 只能是 1/2/3，你传了 {btn_num}")

        btn.hover()
        self.page.wait_for_timeout(500)

        # 悬停后下拉链接出现，用 get_by_role("link") 找可见的链接
        link = self.page.locator(".dropdown-content a").first
        return link.inner_text()
