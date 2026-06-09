import allure 
from playwright.sync_api import Page,expect

@allure.feature("多标签页")
@allure.story("捕获新窗口并操作")
def test_popup_window(page:Page):
    #打开首页
    page.goto("https://webdriveruniversity.com/")

    #2.点击Contact Us，捕获弹出新窗口
    with page.expect_popup() as popup:
        page.click("#contact-us")

    #3.拿到新窗口
    new_page = popup.value
    new_page.wait_for_load_state()

    #4.在新窗口里填表单
    new_page.locator('[name="first_name"]').fill("张三")

    #5.断言
    expect(new_page).to_have_title("WebDriver | Contact Us")