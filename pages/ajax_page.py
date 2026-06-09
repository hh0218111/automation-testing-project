from playwright.sync_api import Page,expect

class Ajax:
    def __init__(self,page : Page):
        self.page = page

        self.click_btn=page.locator("#button1")

    def goto(self):
        self.page.goto("https://webdriveruniversity.com/Ajax-Loader/index.html")

    def wait_btn(self):
        #1.等待按钮出现并点击
        self.click_btn.wait_for(state="visible")
        self.click_btn.click()

        #2.等待弹窗出现
        self.page.wait_for_selector("#myModalClick",state="visible")
        self.page.wait_for_timeout(500)

        #3.读取弹窗标题文字
        modal_title=self.page.locator("#myModalClick .modal-header").inner_text()
        return modal_title