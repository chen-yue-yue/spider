# Scrapy settings for scrapy_cmcc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_cmcc"

SPIDER_MODULES = ["scrapy_cmcc.spiders"]
NEWSPIDER_MODULE = "scrapy_cmcc.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_cmcc (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#1. 随机User-Agent（关键：固定UA必被封，需配合下载中间件）
DOWNLOADER_MIDDLEWARES = {
    # 随机UA中间件（优先级低于默认，确保生效）
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    # 重试中间件（内置，优先开启）
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
    # 禁用默认的User-Agent中间件
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
}
# Concurrency and throttling settings
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16
DOWNLOAD_DELAY = 0.2

# 根据服务器响应速度动态调整延迟，既保证速度又避免被封
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # 初始延迟1秒
AUTOTHROTTLE_MAX_DELAY = 5  # 最大延迟30秒（遇到反爬时自动降速）
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0  # 目标并发（单域名）
AUTOTHROTTLE_DEBUG = False  # 关闭调试，减少日志量

# DNS缓存（海量爬取减少DNS解析耗时）
DNSCACHE_ENABLED = True
DNSCACHE_SIZE = 1000  # 缓存1000个DNS记录
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# 1. 日志配置（海量爬取必须！出问题可排查）
LOG_LEVEL = "DEBUG"  # 只记录INFO及以上（减少日志体积）
#LOG_FILE = "scrapy_cmcc.log"  # 日志写入文件，避免控制台刷屏
#LOG_FILE_APPEND = True  # 追加写入（爬虫中断后重启不覆盖日志）
LOG_ENCODING = "utf-8"

# 2. HTTP缓存（爬取中断后恢复，避免重复爬取已成功的页面）
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # 缓存1天（海量爬取避免重复请求）
HTTPCACHE_DIR = "httpcache"  # 缓存目录
HTTPCACHE_IGNORE_HTTP_CODES = [403, 404, 500]  # 不缓存错误页面
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 3. Item处理（海量数据异步处理，避免阻塞）
CONCURRENT_ITEMS = 100  # 异步处理Item的并发数
# 禁用内存限制（海量数据避免爬虫因内存不足崩溃）
# MEMUSAGE_LIMIT_MB = 1024  # 可选：限制内存使用1G，根据服务器调整

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_cmcc.middlewares.ScrapyCmccSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_cmcc.middlewares.ScrapyCmccDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_cmcc.pipelines.ScrapyCmccPipeline": 300,
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
ITEM_PIPELINES = {
    "scrapy_cmcc.pipelines.ScrapyCmccPipeline":300,
}
