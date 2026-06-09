# import json
# import pytest
# from playwright.sync_api import expect

# def load_json_data():
#     """ 从json文件读测试文件"""
#     with open("data/login_data.json","r",encoding="utf-8") as f:
#         return json.load(f)
    
# @pytest.mark.parametrize("user",load_json_data())
# def test_json_login(test_page,user):
#     """数据驱动 -- 数据来自json"""
#     test_page.locator("#username").fill(user["username"])
#     test_page.locator("#password").fill(user["password"])
#     test_page.locator("#login-btn").click()
#     expect(test_page.locator("#button-result")).to_have_text("✅ 登录按钮被点击了")