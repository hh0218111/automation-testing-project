from playwright.sync_api import Page,expect
import pytest


#region fixture+parametrize 复习
# PAGE_URL="file:///D:/test_locator.html"

# #fixture 练习
# @pytest.fixture
# def test_page(page:Page):
#     """自动打开页面"""
#     page.goto(PAGE_URL)
#     return page

# def text_fix_visible(test_page):
#     btn=test_page.test_locator("#login_btn")
#     expect(btn).to_be_visible()

# #parametrize 练习
# @pytest.mark.parametrize("input_text",[

#     "张三",
#     "admin",
#     "测试用户",
# ])
# def test_para_fill(test_page,input_text):
#     """一份测试跑3组数据"""
#     test_page.locator("#username").fill(input_text)
#     expect(test_page.locator("#username")).to_have_value(input_text)

# #练习3 fixture+parametrize 组合
# @pytest.mark.parametrize("username,password",[
#     ("admin","123"),
#     ("user1","pass1"),
#     ("test","test"),
# ])
# def test_combo(test_page,username,password):
#     test_page.locator("#username").fill(username)
#     test_page.locator("#password").fill(password)
#     test_page.locator("#login-btn").click()

#     expect(test_page.locator("#button-result")).to_have_text("✅ 登录按钮被点击了")
#endregion


"""
用 fixture + parametrize 测试下拉框（选深圳/武汉/成都）
用 fixture + parametrize 测试复选框（勾选编程/游戏/运动）
把 fixture 抽到 conftest.py 里，让两个测试文件都能用
"""
#region fixture+param 练习题1

# Page_url="file:///D:/test_locator.html"

# #fixture 准备前置工作
# @pytest.fixture
# def test_page(page:Page):
#     page.goto(Page_url)
#     return page

# #parametrize 测试多个数据
# @pytest.mark.parametrize("city_value",[
#     "shenzhen",
#     "wuhan",
#     "chengdu",

# ])
# def test_demo(test_page,city_value):
#     dropdown=test_page.locator("#city")
#     dropdown.select_option(city_value)
#     expect(dropdown).to_have_value(city_value)
#endregion


#region fixture+param 练习题2

# @pytest.mark.parametrize("hobby_value",[
#     "coding",
#     "gaming",
#     "sport",
# ])
# def test_demo(test_page,hobby_value):
#     #方式1：用css属性选择器[value = 'coding']
#     checkbox=test_page.locator(f"input[type='checkbox'][value='{hobby_value}']")
#     #方式2：用的是 ID（如 id="hobby-code"） 需要改param参数
#     #checkbox = test_page.locator(f"#hobby-{hobby_value}")
#     checkbox.check() #check不传值
#endregion


#region fixture+param 练习题3
# def test_something(test_page):
#     expect(test_page.locator("#login-btn")).to_be_visible()


""" 题1：写一个完整的 fixture"""

# 要求：打开 WebDriverUniversity 下拉框页面，返回 page
# 命名：wdu_page
# URL：http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html

@pytest.fixture
def wdu_page(page:Page):      # ← 填参数
    page.goto("http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")       # ← 填 URL
    return page          # ← 返回什么？

# 要求：用上面的 fixture，测试下拉框选3种语言
# 数据：python, java, sql  （第一个下拉框的选项）

@pytest.mark.parametrize("subject",["python","java", "sql"])  # ← 填参数名和数据
def test_dropdown(wdu_page, subject):     # ← 填参数名
    dropdown = wdu_page.locator("#dropdowm-menu-1")  # ← 找第一个下拉框
    dropdown.select_option(subject)       # ← 选值
    expect(dropdown).to_have_value(subject) # ← 断言
