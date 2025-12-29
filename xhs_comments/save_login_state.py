from playwright.sync_api import sync_playwright
import json

def save_login_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()
        
        print("请登录小红书，登录成功后按回车键保存登录状态...")
        page.goto("https://www.xiaohongshu.com/explore")
        
        input("登录完成后按回车键...")
        
        storage = context.storage_state(path="xhs_login_state.json")
        print(f"登录状态已保存到 xhs_login_state.json")
        print(f"包含 {len(storage.get('cookies', []))} 个 cookies")
        
        browser.close()

if __name__ == "__main__":
    save_login_state()
