# 这段代码在整个项目中的作用：pytest 自动加载，所有测试文件共享这里的 fixture 和钩子
import pytest
import os

# ========== 钩子：失败自动截图 ==========
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """这段代码的作用：任何测试失败时，自动截图保存到 screenshots/ 目录"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")


# ========== 共享 fixture ==========
# 每个 fixture 的作用：准备页面对象 → 打开网页 → 返回对象给测试用

from pages.ajax_page import Ajax
from pages.contact_page import ContactPage
from pages.datepicker_page import Datepicker
from pages.login_portal import LoginPortalPage
from pages.popup_page import Popup
from pages.wdu_page import WDUDropdownPage
from pages.file_upload_page import fileupload  
from pages.iframe_page import Iframe
from pages.actions_page import ActionsPage
from pages.scroll_page import ScrollPage

@pytest.fixture
def ajax_page(page):
    """AJAX Loader 页面"""
    aj = Ajax(page)
    aj.goto()
    return aj


@pytest.fixture
def contact(page):
    """Contact 联系表单页面"""
    p = ContactPage(page)
    p.goto()
    return p


@pytest.fixture
def date_page(page):
    """Datepicker 日期选择页面"""
    dp = Datepicker(page)
    dp.goto()
    return dp


@pytest.fixture
def portal(page):
    """Login Portal 登录弹窗页面"""
    lp = LoginPortalPage(page)
    lp.goto()
    return lp


@pytest.fixture
def popup_page(page):
    """Popup & Alerts 弹窗页面"""
    p = Popup(page)
    p.goto()
    return p


@pytest.fixture
def wdu(page):
    """Dropdown/Checkbox/Radio 练习页面"""
    p = WDUDropdownPage(page)
    p.goto()
    return p

@pytest.fixture
def iframe_page(page):
    If=Iframe(page)
    If.goto()
    return If


@pytest.fixture
def file_page(page):
    """File Upload 文件上传"""
    fu = fileupload(page)
    fu.goto()
    return fu


@pytest.fixture
def actions_page(page):
    """Actions 高级交互页面（拖拽/双击/按住/悬停）"""
    ap = ActionsPage(page)
    ap.goto()
    return ap

@pytest.fixture
def scroll_page(page):
    """Scroll 页面滚动"""
    sp=ScrollPage(page)
    sp.goto() 
    return sp
