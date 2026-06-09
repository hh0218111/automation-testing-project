from playwright.sync_api import Page,expect
class ScrollPage:
    def __init__(self,page:Page):
        self.page = page

        self.zone1=page.locator("#zone1")
        self.zone2_entries = page.locator("#zone2-entries")
        self.zone3_entries = page.locator("#zone3-entries")
        self.zone4 = page.locator("#zone4")

    def goto(self):
        self.page.goto("https://webdriveruniversity.com/Scrolling/index.html")
    
    def do_scroll_zone2(self):
        #1.滚动到 zone2 可见
        zone2_text=self.zone2_entries.scroll_into_view_if_needed()
        #2.等 300ms
        self.page.wait_for_timeout(300)
        #3.bounding_box() 拿坐标
        box=self.zone2_entries.bounding_box()
        #4.mouse.move() 移到中心点
        self.page.mouse.move(box["x"] + box["width"] /2,box["y"] + box["height"] /2)
        #5.等 500ms
        self.page.wait_for_timeout(500) 
        #6.return zone2_entries 的文字
        zone2_text = self.zone2_entries.inner_text()
        #返回文字
        return  zone2_text

    def do_scroll_zone3(self):
        #1.滚动到 zone3 可见
        zone3_text=self.zone3_entries.scroll_into_view_if_needed()
        #2.等 300ms
        self.page.wait_for_timeout(300)
        #3.bounding_box() 拿坐标
        box=self.zone3_entries.bounding_box()
        #4.mouse.move() 移到中心点
        self.page.mouse.move(box["x"] + box["width"] /2,box["y"]  + box["height"] /2)
        #5.等 500ms
        self.page.wait_for_timeout(500) 
        #6.return zone2_entries 的文字
        zone3_text = self.zone3_entries.inner_text()
        #返回文字
        return  zone3_text
    
    def do_zone4(self):
        #1.滚动到 zone4 可见
        zone4_text=self.zone4.scroll_into_view_if_needed()
        #2.等 300ms
        self.page.wait_for_timeout(300)
        #3.bounding_box() 拿坐标
        box = self.zone4.bounding_box()
        #4.mouse.move() 移到中心点
        self.page.mouse.move(box["x"] + box["width"] /2,box["y"] + box["height"] /2)
        #5.等 500ms
        self.page.wait_for_timeout(500) 
        #6.return zone2_entries 的文字
        zone4_text = self.zone4.inner_text()
        #返回文字
        return  zone4_text






