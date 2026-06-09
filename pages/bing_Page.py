from playwright.sync_api import Page, expect
import time

class BingPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("#sb_form_q")

    def goto(self):
        """打开必应，关闭可能出现的弹窗"""
        self.page.goto("https://www.bing.com/?mkt=en-US", wait_until="domcontentloaded")
        # 等待页面稳定
        self.page.wait_for_selector("#sb_form_q", state="visible", timeout=10000)
        # 尝试关闭隐私/通知弹窗（常见选择器）
        close_buttons = [
            "button:has-text('接受')",
            "button:has-text('同意')",
            "button:has-text('关闭')",
            "#bnp_btn_accept",
            "[aria-label='关闭']"
        ]
        for selector in close_buttons:
            try:
                if self.page.locator(selector).count():
                    self.page.locator(selector).click(timeout=2000)
                    time.sleep(0.5)  # 给弹窗关闭动画时间
            except:
                pass

    def search(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_input.press("Enter")
        # 关键修改：等待 b_algo 元素存在即可（不要求可见），因为有时是父容器隐藏但文本可读
        self.page.wait_for_selector(".b_algo", state="attached", timeout=15000)
        # 额外等待一小段时间，让可能的覆盖层消失
        self.page.wait_for_timeout(2000)
        # 调试：截图查看当前状态
        self.page.screenshot(path="bing_search_debug.png")

    def get_first_result_text(self) -> str:
        first_result = self.page.locator(".b_algo h2 a").first
        return first_result.inner_text()

    def assert_has_result(self, keyword: str):
        # 断言页面包含关键词（即使元素不可见，文本依然存在）
        expect(self.page.locator("body")).to_contain_text(keyword)