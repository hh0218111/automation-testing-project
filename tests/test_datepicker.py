# conftest.py 提供 date_page fixture
import pytest
import yaml
import allure

@allure.feature("日期选择")      
@allure.story("选指定日期")

def date_data_yaml():
    with open("data/datepicker_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("dates", date_data_yaml())
def test_datepicker(date_page, dates):
    date_page.pick_date(dates["date"])
    date_page.assert_date(dates["expected"])
