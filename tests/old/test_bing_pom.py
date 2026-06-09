from playwright.sync_api import Page
from pages.bing_Page import BingPage 

def test_bing_search_pom(page:Page):
    bing=BingPage(page)
    bing.goto()
    bing.search("playwright")
    #断言搜索结果包含关键词
    bing.assert_has_result('playwright')