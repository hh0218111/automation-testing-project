import pytest
from playwright.sync_api import Page,expect
from pages.scroll_page import ScrollPage


def test_scroll(scroll_page):
    text = scroll_page.do_scroll_zone2()
    assert "Entries" in text

    text1 = scroll_page.do_scroll_zone3()
    assert  "Entries" in text1

    ares = scroll_page.do_zone4()
    assert  "X"  in ares