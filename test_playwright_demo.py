# 逐行对应：导入 → 启动 Playwright → 开浏览器 → 开新标签页 → 访问网址 → 打印标题 → 关浏览器
from playwright.sync_api import sync_playwright  # 难记死了，sync = 同步模式

def test_baidu_titile():
    with sync_playwright() as p :  # 启动引擎，通with open。with负责用完后自动关闭
        browser = p.chromium.launch()  # 打开浏览器
        page = browser.new_page()  #新建标签页
        page.goto("https://www.baidu.com")  # 在标签页里访问网址
        print(page.title())   # 访问后，打印网址标题
        browser.close()   #关闭浏览器
