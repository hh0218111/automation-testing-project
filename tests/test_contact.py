# conftest.py 提供 contact fixture
import pytest
import yaml
import allure

@allure.feature("表单提交")       
@allure.story("	联系表单数据驱动")

def load_data_yaml():
    with open("data/contact_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("user", load_data_yaml())
def test_contact_form(contact, user):
    contact.fill_form(user["first"], user["last"], user["email"], user['message'])
    contact.submit()
    contact.assert_success()
