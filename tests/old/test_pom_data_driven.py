""" POM+数据驱动 -- 面试最爱组合"""

import yaml
import pytest
from pages.login_page import LoginPage

def load_yaml_data():
    with open("data/login_data.yaml","r",encoding="utf-8") as f:
        return yaml.safe_load(f)
    
@pytest.mark.parametrize("user",load_yaml_data())
def test_pom_with_data(page,user):
    """ POM页面类 + YAML数据文件"""
    lp=LoginPage(page)
    lp.goto()
    lp.login(user["username"],user["password"])
    lp.assert_login_clicked()