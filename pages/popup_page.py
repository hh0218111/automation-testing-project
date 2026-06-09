from playwright.sync_api import Page

class Popup:
    def __init__(self, page: Page):
        self.page = page
        self.alert_btn = page.locator("#button1")
        self.confirm_btn = page.locator("#button4")
        self.result_text = page.locator("#confirm-alert-text")

    def goto(self):
        """打开弹窗测试页面"""
        self.page.goto("https://webdriveruniversity.com/Popup-Alerts/index.html")

    def click_alert(self):
        result={"msg" : ""}
        def handle_dialog(dialog):
            result["msg"] = dialog.message
            dialog.accept()
        self.page.once("dialog",handle_dialog)
        self.alert_btn.click()
        self.page.wait_for_timeout(500)


        return result ["msg"]#返回弹窗文字


    def click_confirm(self,accept=True):

        result={"msg":" " ,"result_text" : " "}

        def handle_dialog(dialog):
            result["msg"] = dialog.message
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog",handle_dialog)
        self.confirm_btn.click()
        self.page.wait_for_timeout(500)
        
        # 获取页面上显示的"OK"或"Cancel"文字，存到字典里。
        result["result_text"] = self.result_text.inner_text()
        return result