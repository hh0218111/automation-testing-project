from playwright.sync_api import expect,Page

class SearchPage:
    def __init__(self,page:Page):
        self.page=page

        #定位器集中管理
        self.search_box=page.locator(".search-box") #属性名

    def goto(self):
        #打开网页
        self.page.goto("file:///D:/test_locator.html")

    
    def search(self, keyword : str): #方法名
        self.search_box.fill(keyword)
        # self.search.press("Enter") #本地html搜索框没有绑键盘事件，回车没有用

    #断言成了"测浏览器"，不是测页面
    # def assert_search(self, keyword : str):
    #     expect(self.search).to_have_value(keyword)

    def assert_search(self, keyword: str):
        """断言搜索框的值是 keyword"""
        expect(self.search_box).to_have_value(keyword)
