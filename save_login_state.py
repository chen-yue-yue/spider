import asyncio
from playwright.async_api import async_playwright


async def save_xhs_login_state():
    async with async_playwright() as p:
        # 启动有头浏览器，模拟真实环境
        browser = await p.chromium.launch(
            headless=False,
            args=["--no-sandbox", "--start-maximized"]
        )
        # 创建浏览器上下文（保存登录态的核心）
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # 访问小红书
        await page.goto("https://www.xiaohongshu.com/explore", wait_until="networkidle")

        # 暂停程序，让你手动登录（输入手机号/验证码/密码）
        print("请在浏览器中完成小红书登录，登录成功后按回车继续...")
        input()

        # 保存完整登录态到文件（包含Cookie、localStorage等）
        await context.storage_state(path="xhs_comments/xhs_login_state.json")
        print("✅ 登录态已保存到 xhs_login_state.json")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(save_xhs_login_state())