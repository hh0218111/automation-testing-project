from playwright.sync_api import Page,expect

class ContactPage:
    def __init__(self,page:Page):
        self.page=page
        
        self.first_name = page.locator("[name='first_name']")
        self.last_name = page.locator('[name="last_name"]')
        self.email = page.locator('[name="email"]')
        self.comment = page.locator('[name="message"]')
        self.submit_btn=page.locator('[type="submit"][value="SUBMIT"]')#更精准定位

    def goto(self): 
        self.page.goto(" http://webdriveruniversity.com/Contact-Us/contactus.html ")

    def fill_form(self,first,last,email,comment):
        """ 填写表单"""
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.comment.fill(comment)

    def submit(self):
        """ 点击提交"""
        self.submit_btn.click()

    def assert_success(self):
        """ 断言提交成功"""
        expect(self.page.locator("#contact_reply")).to_contain_text("Thank You")