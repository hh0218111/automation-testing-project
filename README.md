# 自动化测试项目

## 简介
基于 **Playwright + pytest + Allure** 的 Web UI 自动化测试项目。
对 [WebDriverUniversity.com](https://webdriveruniversity.com/) 的 10 个页面进行了完整的端到端自动化测试。

## 技术栈
- **Python 3.13** — 编程语言
- **Playwright** — 浏览器自动化
- **pytest** — 测试框架
- **Allure** — 测试报告
- **YAML** — 测试数据驱动

## 项目结构
```
├── pages/          # 页面对象模型（POM），封装页面操作
│   ├── contact_page.py
│   ├── login_portal.py
│   ├── popup_page.py
│   ├── actions_page.py
│   └── ...
├── tests/          # 测试用例
│   ├── conftest.py         # 共享 fixture + 失败截图钩子
│   ├── test_contact.py
│   ├── test_popup.py
│   ├── test_actions.py
│   ├── test_route_mock.py  # 网络拦截
│   ├── test_multitab.py    # 多标签页
│   └── ...
├── data/           # 测试数据（YAML 文件）
└── pytest.ini      # pytest 配置
```

## 如何运行

```bash
# 1. 安装依赖
pip install pytest playwright allure-pytest pyyaml

# 2. 安装浏览器
playwright install chromium

# 3. 运行所有测试
pytest tests/ -v

# 4. 生成 Allure 测试报告
pytest tests/ --alluredir=allure-results
allure serve allure-results

# 5. 查看录屏（自动保存到 videos/ 目录）
# 查看追踪：playwright show-trace traces/trace.zip
```

## 测试覆盖

### 页面交互（10 个页面）
| 页面 | 技能点 |
|------|--------|
| Dropdown / Checkbox / Radio | select_option, check |
| Contact Us 表单 | POM + YAML 数据驱动 |
| Login Portal | Alert 弹窗处理 |
| Popup & Alerts | confirm accept/dismiss |
| Datepicker | 日期选择 |
| AJAX Loader | wait_for_selector 显式等待 |
| iframe | frame_locator 跨域操作 |
| File Upload | set_input_files 文件上传 |
| Actions | drag_to, dblclick, hover, mouse.down/up |
| Scrolling | scroll_into_view, mouse.move |

### 高级技能
| 技能 | 说明 |
|------|------|
| 网络拦截 mock | page.route() + route.fulfill() 模拟 API 返回 |
| 网络拦截 abort | page.route() + route.abort() 屏蔽图片请求 |
| 多标签页切换 | page.expect_popup() 捕获新窗口 |
| 录屏 | browser.new_context(record_video_dir=...) 保存测试视频 |
| 追踪 debug | context.tracing.start() 生成 trace.zip |
| 数据驱动 | YAML 文件分离测试数据 |
| POM 设计模式 | 页面操作与测试逻辑分离 |
| 失败自动截图 | conftest 钩子自动保存失败截图 |
