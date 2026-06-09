# conftest.py 提供 ajax_page fixture
import allure

@allure.feature("异步加载")      
@allure.story("	Modal 弹窗等待")

def test_ajax(ajax_page):
    title = ajax_page.wait_btn()
    print(f"弹窗标题: {title}")
    assert "Well Done" in title
