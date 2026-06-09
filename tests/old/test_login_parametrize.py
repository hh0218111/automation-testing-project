import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password",[
    ("admin","123"),
    ("user1","pass1"),
    ("test","test"),
])

def test_login_multiple_user(page:Page,username,password):
    lp=LoginPage(page)
    lp.goto()
    lp.login(username,password)
    lp.assert_login_clicked()