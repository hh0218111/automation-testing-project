from playwright.sync_api import Page,expect

class fileupload:
    def __init__(self,page:Page):
        self.page=page
        
        # 这段代码的作用：选择文件上传
        self.file=self.page.locator("input[type='file']")
        #提交按钮
        self.submit_btn = self.page.locator("#submit-button")
    def goto(self):
        self.page.goto("https://webdriveruniversity.com/File-Upload/index.html")

    def upload_file(self,file_path: str):
        """这段代码的作用：选择文件并上传，返回弹窗消息"""
        #1.选择文件(直接设置路径，不用点击)
        self.file.set_input_files(file_path)

        #2.准备接受弹窗
        result ={"msg": ""}  #参考了popup_page.py
        def handle_dialog(dialog):
            result ["msg"]=dialog.message
            dialog.accept()
        self.page.once("dialog",handle_dialog)

        #3.点击提交
        self.submit_btn.click()
        self.page.wait_for_timeout(1000)

        return result["msg"]




