import allure
from playwright.sync_api import Page


@allure.feature("网络拦截")
@allure.story("拦截真实 API，返回假数据")
def test_route_mock(page: Page):
    """最简单版本：看懂每一行再改"""

    # ====== 1. 往页面里塞一段 HTML（一个按钮 + 一个显示区） ======
    # page.setContent() = 直接往浏览器里写网页内容
    page.set_content("""
        <button id="btn">点我加载数据</button> 
        <div id="result" style="margin-top:10px;font-size:18px;"></div>
        <script>
            document.getElementById("btn").onclick = async function() {
                let res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
                let data = await res.json();
                document.getElementById("result").innerText = JSON.stringify(data);
            };
        </script>
    """)

    # ====== 2. 拦截！ ======
    # 凡是请求网址里包含 "jsonplaceholder.typicode.com" 的
    # 都不让发出去，直接返回我编的假数据
    page.route("**/jsonplaceholder.typicode.com/**", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='{"title": "你好世界", "id": 123}'
    ))

    # ====== 3. 点击按钮（触发上面的 fetch） ======
    page.locator("#btn").click()
    page.wait_for_timeout(1000)

    # ====== 4. 看页面上显示的是不是假数据 ======
    text = page.locator("#result").inner_text()
    print(f"页面显示：{text}")

    assert "你好世界" in text, f"拦截失败！实际内容：{text}"
