from playwright.sync_api import Page,expect
class Iframe:
    def __init__(self ,page:Page):
        self.page = page

        # 这段代码在整个页面中的作用：切换到 iframe 内部，才能操作里面的元素
        self.frame= self.page.frame_locator("#frame") #定位iframe
        
        # 这段代码在整个页面中的作用：在 iframe 里点击按钮
        self.frame_btn=self.frame.locator("#button-find-out-more")
    
    def goto(self):
        self.page.goto("https://webdriveruniversity.com/IFrame/index.html")

    def do_iframe(self):
        #1.点击 iframe 里找按钮
        self.frame_btn.click()

        #2。等待弹窗出现(在主页面)
        self.frame.locator("#myModal").wait_for(state="visible")
        self.page.wait_for_timeout(500)

        #读取弹窗标题文字
        title=self.frame.locator("#myModal .modal-header").inner_text()
        return title


