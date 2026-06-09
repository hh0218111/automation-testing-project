from pages.search_page import SearchPage
from playwright.sync_api import Page,expect

def test_search(page:Page):
    sp=SearchPage(page)
    sp.goto()
    sp.search("pytest")
    # 断言写在测试里，不在页面类里
    sp.assert_search("pytest")