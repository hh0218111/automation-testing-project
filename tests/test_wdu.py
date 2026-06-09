# conftest.py 提供 wdu fixture
import pytest
from playwright.sync_api import expect
import allure

@allure.feature("表单控件")       
@allure.story("	下拉框/复选框/单选")

@pytest.mark.parametrize("value", ["python", "java", "c#"])
def test_dropdown(wdu, value):
    wdu.select_language(value)
    expect(wdu.dropdown1).to_have_value(value)

@pytest.mark.parametrize("num", [1, 2, 3, 4])
def test_checkbox(wdu, num):
    wdu.check_option(num)
    checkbox = getattr(wdu, f"checkbox{num}")
    expect(checkbox).to_be_checked()

@pytest.mark.parametrize("color", ["green", "blue"])
def test_radio(wdu, color):
    wdu.select_color(color)
    radio = getattr(wdu, f"radio_{color}")
    expect(radio).to_be_checked()
