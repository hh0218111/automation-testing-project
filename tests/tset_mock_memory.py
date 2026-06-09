from playwright.sync_api import Page,expect

def test_mock(page:Page):
    page.set_content("""
    <button id="fetch">加载用户</button>
    <div id="output"></div>
    <script>
        document.getElementById("fetch").onclick = async function() {
            let res = await fetch("https://jsonplaceholder.typicode.com/users/1");
            let data = await res.json();
            document.getElementById("output").innerText = data.name;
        };
    </script>
""")
    page.route("**/jsonplaceholder.typicode.com/**",lambda route:route.fulfill(
        body='{"name":"主公写的"}'

    ))
    
    #点击按钮
    page.locator("#fetch").click()

    #断言
    assert "主公" in page.locator("#output").inner_text()

    