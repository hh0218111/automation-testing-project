from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_login_with_pom(page:Page):
    """  用pom方式测试登录"""

    lp=LoginPage(page)
    lp.goto()
    lp.login("admin","123")
    lp.assert_login_clicked()