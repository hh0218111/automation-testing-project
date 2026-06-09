import allure
from playwright.sync_api import Page


def test_route_mock(page:Page):
    page.set_content("""
    <button id="load">加载用户</button>
<div id="out"></div>
<script>
document.getElementById("load").onclick = async function() {
    let res = await fetch("https://jsonplaceholder.typicode.com/users/1");
    let data = await res.json();
    document.getElementById("out").innerText = data.name;
};
</script>
""")
    
    #2.拦截
    page.route("**/jsonplaceholder.typicode.com/**", lambda route: route.fulfill(
        body='{"name": "主公"}'))

    #3点击按钮
    page.locator("#load").click()

    #4.看页面假数据 

    assert "主公" in page.locator("#out").inner_text()