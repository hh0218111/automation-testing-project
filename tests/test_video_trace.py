import os 

#测试1：录屏
def test_record_video(browser):
    #1.创建录屏上下文

    os.makedirs("videos",exist_ok=True)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    #2.操作
    page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")
    page.locator('[name="first_name"]').fill("张三")

    #3.关闭  ->  视频保存
    path=page.video.path()
    print(f"视频：{path}")
    context.close()

    #4.断言文件存在
    assert os.path.exists(path)


#测试2：追踪
def test_tracing(browser):
    #1.开启追踪
    os.makedirs("traces",exist_ok = True)
    context = browser.new_context()
    context. tracing.start(screenshots=True,snapshots=True)
    page = context.new_page()

    #2.操作
    page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")  
    page.locator('[name="first_name"]').fill("追踪测试")
    page.locator('[name="message"]').fill("trace内容")
    page.locator('[type="submit"]').click()
    page.wait_for_timeout(1000)


    #3.保存追踪文件
    context.tracing.stop(path="traces/trace.zip")
    context.close()

    assert os.path.exists("traces/trace.zip")

