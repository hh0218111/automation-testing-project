import yaml
import pytest
from playwright.sync_api import expect

def load_yaml_data():
    """ 从yaml读取测试文件"""
    with open("data/login_data.yaml","r",encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize("user",load_yaml_data())
def test_yaml_login(test_page,user):
    """ 数据驱动 -- 数据来自yaml文件"""
    test_page.locator("#username").fill(user["username"])
    test_page.locator("#password").fill(user["password"])
    test_page.locator("#login-btn").click()

    expect(test_page.locator("#button-result")).to_have_text("✅ 登录按钮被点击了")
