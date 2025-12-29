# Scrapy settings for scrapy_lianjia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_lianjia"

SPIDER_MODULES = ["scrapy_lianjia.spiders"]
NEWSPIDER_MODULE = "scrapy_lianjia.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_lianjia (+http://www.yourdomain.com)"

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 2.0

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Cookie":"SECKEY_ABVK=vvR+KBylzs341tIeurubnC63QkuzoCT4z28NwsewLu8%3D; BMAP_SECKEY=HONR2i8zc6cMsGE7x3f74kMeK0YTAPBcnmTv7Gp0Ro5gleGJusap5tyBcSMGE-obRC3mH_rO9q1uFNX8o4vniGg3BXqwWSPWmYy9xWEYEDzh6xCMRN3c8ns-7UMcyFVGUsaVrpKtg-4nCa82C6KUWkAoFKVLIrd5G-_8ZybetM9-OhdOQsFf56b3SVbb_Ad9; lianjia_uuid=d929ba72-679f-4718-8933-4901ec4ff338; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219b0c307531211-0ff3e212874-26061b51-1821369-19b0c30753222cd%22%2C%22%24device_id%22%3A%2219b0c307531211-0ff3e212874-26061b51-1821369-19b0c30753222cd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; crosSdkDT2019DeviceId=-t4vocm--1vlpj0-oiejge3gamr0gu6-h87tudo0r; _ga=GA1.2.1772040068.1765436072; _gid=GA1.2.1003414472.1765436072; ftkrc_=58a7b8d4-022b-42ee-90c9-4bcdb435ca79; lfrc_=5a67ae8f-1cf4-4aa8-96c3-4b86f1901c30; select_city=110000; _jzqckmp=1; login_ucid=2000000483328062; lianjia_token=2.0012f6530b47bc3ed9035b7a3a3e971a69; lianjia_token_secure=2.0012f6530b47bc3ed9035b7a3a3e971a69; security_ticket=IeBuEYZ747wMIWqW31xzPZqZBcTgouskFZujcwMRrieoCMOitoS7JbKlPWhUFj5WKuyueFBXA3wJGocJaaq12I4WzdmU5kN9CN0YolrktKv+adjpeAhGPsUGwhZekxIfSXirVYnl+z5bxPUArz7G25i+owzAMZ/cvnDvvADKKVU=; _jzqx=1.1765453672.1765601153.4.jzqsr=bj%2Elianjia%2Ecom|jzqct=/.jzqsr=clogin%2Elianjia%2Ecom|jzqct=/; lianjia_ssid=a132d1b0-f76e-4d62-9683-44a6aa845c58; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1765456879,1765514166,1765589539,1765612406; HMACCOUNT=3F18AC6E8ACD690D; _qzjc=1; _jzqa=1.787719326959594200.1765436061.1765601153.1765612406.11; _jzqc=1; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1765612524; _qzja=1.1379139782.1765436061258.1765601152811.1765612406196.1765612430083.1765612523780.0.0.0.64.11; _qzjb=1.1765612406196.5.0.0.0; _qzjto=14.4.0; _jzqb=1.5.10.1765612406.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZjg1ZjllNDhjZjM2ZDNjZTE0ZjI1OTVjNmNhNjM0ZDFmNTZhNGJkMWY1OGQ5MDdmMmFjMjBkYWRhOWRhZTg1Njg0NGMyNzBjOGU1NTIwYTcyM2VlNjMwYmE5OWY1NDA1NTY1ZGVkOGY0MDI3MmI5MTlmZjY0YjA3YzVmNzEyMWQ2ZmE1MDljNjNjMWE5OTIwNmNkNWM4MmUwMzFjNGNjZTg1MzBiMTVjOGE3NDY1MjFjMWI0MjRkNDEyYmE1OTA2N2VlN2RiOTM4ZGMwZWU3YmIwNzkxNWMxNmIwY2Q4Nzg1OWM2MTFmNGQ0YzZkZmM2NmM0YTdiNzIxYWVhZTBlOFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJlMTQ0YTY1NFwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcGcxLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_KJTRWRHDL1=GS2.2.s1765612419$o8$g1$t1765612534$j60$l0$h0; _ga_QJN1VP0CMS=GS2.2.s1765612419$o8$g1$t1765612534$j60$l0$h0",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Referer":"https://hip.lianjia.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}



# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_lianjia.middlewares.ScrapyLianjiaSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy_lianjia.middlewares.ScrapyLianjiaDownloaderMiddleware": None,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_lianjia.pipelines.ScrapyLianjiaPipeline": 300,
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

# Set log level to INFO to see our log messages
LOG_LEVEL = "DEBUG"

ITEM_PIPELINES = {
    "scrapy_lianjia.pipelines.ScrapyLianjiaPipeline":300,
}

REDIRECT_ENABLED = False
HTTPERROR_ALLOWED_CODES = [302]