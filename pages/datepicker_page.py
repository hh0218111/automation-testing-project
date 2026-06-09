from playwright.sync_api import Page,expect

class Datepicker:
    def __init__(self,page : Page):
        self.page = page
        self.date_btn=page.locator(".form-control")

    def goto(self):
        self.page.goto("https://webdriveruniversity.com/Datepicker/index.html")

    def pick_date(self,date_str: str):
        """ date_str = '2026-06-15' """
        #1.打开日历
        self.date_btn.click()
        self.page.wait_for_timeout(500)

        #2.从“2026——06-15” 里取出 “15”
        day = date_str.split("-")[-1] 

        #3.点日历上的那一天
        self.page.get_by_role("cell",name=day).click() #只在日历格子里 找

        

    def assert_date(self,expected_date):
        expect(self.date_btn).to_have_value(expected_date)