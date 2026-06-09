# conftest.py 提供 popup_page fixture
import pytest
import yaml
import allure

@allure.feature("弹窗处理")   
@allure.story("	JS Confirm OK/Cancel") 

def popup_data():
    with open("data/popup_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("dialogs", popup_data())
def test_popup(popup_page, dialogs):
    if dialogs["dialog_type"] == "alert":
        popup_page.click_alert()

    elif dialogs["dialog_type"] == "confirm":
        accept = dialogs["action"] == "accept"
        result = popup_page.click_confirm(accept=accept)

        assert dialogs["expected_msg"] in result["msg"]
        assert dialogs["expected_result"] in result["result_text"]
