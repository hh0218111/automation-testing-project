# conftest.py 提供 portal fixture
import pytest
import yaml
import allure

@allure.feature("弹窗处理")   
@allure.story("	JS Alert 登录验证") 

def load_data_yaml():
    with open("data/login_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("users", load_data_yaml())
def test_login_with_portal(portal, users):
    msg = portal.login(users["username"], users["password"])

    if users["expected"] == 'success':
        portal.assert_success(msg)
    else:
        portal.assert_fail(msg)
