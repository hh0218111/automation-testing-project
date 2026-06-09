import pytest
from pages.file_upload_page import fileupload
from playwright.sync_api import Page
import allure

@allure.feature("文件上传")        
@allure.story("上传文件断言弹窗")         


def test_upload(file_page):
    msg =file_page.upload_file(r"C:\Users\ATI\Desktop\万能排查 SOP.txt")
    assert "uploaded!" in msg
    