# 写 tests/test_route_abort.py：

# 用 route.abort() 屏蔽所有 .png 和 .jpg 图片
# 打开 https://webdriveruniversity.com/（首页有很多图片）
# 断言页面标题仍是 "WebDriverUniversity.com"（说明页面本身还能加载，只是没图片）
# 提示：page.route() 必须写在 page.goto() 前面。
import allure
from playwright.sync_api import Page,expect

@allure.feature("网络拦截")
@allure.story("route abort 屏蔽图片")
def test_route_abort(page:Page):
    #屏蔽所有图片的请求
    page.route("**/*.png",lambda route:route.abort())
    page.route("**/*.jpg",lambda route:route.abort())

    #2.打开wdu首页
    page.goto("https://webdriveruniversity.com/")

    #3.页面标签还在，说明页面本身没问题
    expect(page).to_have_title("WebDriverUniversity.com")
