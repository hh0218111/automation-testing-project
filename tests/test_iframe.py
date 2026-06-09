import pytest
from playwright.sync_api import Page
from pages.iframe_page import Iframe
import allure

@allure.feature("跨域操作")      
@allure.story("iframe 内元素交互")

def test_iframe(iframe_page):
    title_text=iframe_page.do_iframe()
    print(f"弹窗标题是：{title_text}")

    assert "Welcome" in title_text  