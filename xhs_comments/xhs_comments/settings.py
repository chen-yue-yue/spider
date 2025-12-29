# Scrapy settings for xhs_comments project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "xhs_comments"

SPIDER_MODULES = ["xhs_comments.spiders"]
NEWSPIDER_MODULE = "xhs_comments.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "xhs_comments (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_DOMAIN = 4
DOWNLOAD_DELAY = 0.4
RANDOMIZE_DOWNLOAD_DELAY = True

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
#  反应堆配置
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# Override the default request headers:
# 启用playwright扩展
DEFAULT_REQUEST_HEADERS = {
    "Cookie":"abRequestId=76fdf6ce-1d25-57c6-ba6b-be434462fb8e; xsecappid=xhs-pc-web; a1=19b590c4ba3zxx6opgphqj5m1ouoeiy17ro04a38n50000307578; webId=3531ad7fde17ed74023408f1a9b84c35; gid=yjD2j8SKy2WfyjD2j8S4DF0q0quCCKlUkUxAlYIV26yl7828ld3vy4888q8W2WY8dqdi0jJK; acw_tc=0a00d2b017667491406296651ef6f313e3a0209b60ab031afede1232c52a4b; webBuild=5.3.0; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=1ac08fdc-c621-4dbb-818f-ae3d9048d0df; loadts=1766749282555; web_session=040069b1a924e1578546183c7b3b4b8e3d4100; id_token=VjEAAOF7xxno0/f/skjNgfDuuIYw7dsdP7BaYJ/2wygDKBAWnU+jMtx75wjwq0LosS1lU0lsIN2PVilgVwOa821qUS0SuK5bmPJ9ktw8ds/n1mvs608rAM0paF/MM6K/8grWSUBm; unread={%22ub%22:%22694b7f9e000000001e015124%22%2C%22ue%22:%22694a59e7000000001e0080bd%22%2C%22uc%22:14}",
 }

#随机User-Agent（关键：固定UA必被封，需配合下载中间件）
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
USER_AGENTS_ENABLED = True
# 只保留主流浏览器和设备
USER_AGENT_TYPES = [
    'chrome', 'firefox', 'safari',  # 浏览器
    'windows', 'macos', 'iphone', 'android'  # 设备
]
# 允许异步操作
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Playwright 核心配置
PLAYWRIGHT_BROWSER_TYPE = "chromium"
#设置Playwright的浏览器参数
PLAYWRIGHT_CONTEXTS = {
    'default': {
        'storage_state': 'xhs_login_state.json', # 登录态放在这
        'viewport': {'width': 1920, 'height': 1080},
        # UA 最好在这里固定一个最近版本的真实浏览器 UA
        'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
}
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": False,
    "args": [
        "--no-sandbox",
        "--disable-blink-features=AutomationControlled",
        "--start-maximized",
        "--kiosk"
    ]
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "xhs_comments.middlewares.XhsCommentsSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "xhs_comments.middlewares.XhsCommentsDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "xhs_comments.pipelines.XhsCommentsPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
LOG_LEVEL = "INFO"
