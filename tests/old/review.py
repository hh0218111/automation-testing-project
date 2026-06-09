"""
# 要求：测试下拉框选"武汉"，勾选"游戏"复选框，输入用户名"张三"。
"""
import pytest
from playwright.sync_api import expect
import yaml
#region 练习2：手写一个完整测试（不看任何参考）

# @pytest.mark.parametrize("city,hobby,name",[  # ← 逗号在字符串里，不是分开的字符串
#     ("wuhan","gaming","张三"),

# ])
# def test_demo(test_page,city,hobby,name):

#     #下拉框
#     city_value=test_page.locator("#city")
#     city_value.select_option(city)
#     expect(city_value).to_have_value(city)


#     #复选框
#     checkbox=test_page.locator(f"input[value='{hobby}']")# ← 用 f-string 插变量
#     checkbox.check()
#     expect(checkbox).to_be_checked()


#     #输入框
#     test_page.locator("#username").fill(name)  # ← 加 .locator
#     expect(test_page.locator("#username")).to_have_value(name)
#endregion


"""
**原代码（你已会的）**：
```python
def test_login(test_page):
    test_page.locator("#username").fill("admin")
    test_page.locator("#login-btn").click()
```
**变化1**：用户名改成读文件里的数据
**变化2**：加上"先清空再输入"
**变化3**：点击前先断言按钮可见，点击后断言文字变化
"""
#region 练习3：改代码——我能适应变化吗？

#**变化1**：用户名改成读文件里的数据
def  load_yaml_data():
    with open("data/login_data.yaml","r",encoding="utf-8") as f :
        return yaml.safe_load(f)
    
@pytest.mark.parametrize("user",load_yaml_data())    
def test_login(test_page,user):
    #**变化2**：加上"先清空再输入"
    #定位#username
    username=test_page.locator("#username")
    #清空
    username.clear()
    #在输入
    username.fill(user["username"])

    #**变化3**：点击前先断言按钮可见
    btn=test_page.locator("#login-btn")
    expect(btn).to_be_visible()
    btn.click()

    #点击后断言文字变化
    expect(test_page.locator("#button-result")).to_have_text("✅ 登录按钮被点击了")
# endregion


"""
## 练习4：POM 变体——把搜索框也封装成类

本地 HTML 里有一个搜索框（`class="search-box"`）。
写出 `SearchPage` 类，包含：
- `__init__`：定位搜索框
- `search(keyword)`：输入关键词 + 按回车

```python
# pages/search_page.py
class SearchPage:
    ...
```

"""