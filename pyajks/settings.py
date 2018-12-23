# -*- coding: utf-8 -*-

# Scrapy settings for pyajks project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pyajks'
SPIDER_MODULES = ['pyajks.spiders']
NEWSPIDER_MODULE = 'pyajks.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pyajks (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    ':authority':'jinan.anjuke.com',
    ':method': 'GET',
    ':scheme': 'https',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Cache-Control': "max-age=0",
    'Connection': 'keep-alive',
    'cookie':'aQQ_ajkguid=69B62F71-375A-A508-59FE-0F99C0F9494C; 58tj_uuid=9c0a630a-2ffb-4f8a-8f60-5ab0bbeb8299; als=0; sessid=03E0BE49-01D2-DF2F-0A5B-F0767A83E8CA; lps=http%3A%2F%2Fwww.anjuke.com%2F%7C; twe=2; _ga=GA1.2.1097229800.1545307123; wmda_uuid=40dfb4a1793b932235754077de82a99d; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; ajk_member_captcha=1183ef14d23a499b27985501748cf2ae; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1545539405; ctid=23; lp_lt_ut=a74310566e44864fd4006036e8ca8f23; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1545539472; wmda_session_id_6289197098934=1545541833836-650590b5-1a6a-309a; _gid=GA1.2.1071844985.1545541835; init_refer=https%253A%252F%252Fjinan.anjuke.com%252F; new_uv=2; new_session=0; __xsptplusUT_8=1; browse_comm_ids=951802%7C1043629%7C835332%7C1030008%7C1016438; propertys=pd87v4-pk6fnt_pa2b6i-pk6fhk_p9jb7l-pk6djw_p5hv44-pk6bp8_p75z04-pk1eiw_pesh0s-pk1bhj_p7ov9c-pk1bge_p132wo-pk1ao0_; _gat=1; __xsptplus8=8.3.1545541841.1545546976.23%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23neTZvcqffKnXMpH5FOpiRtkPacZBGib1%23'
}
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pyajks.middlewares.PyajksSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'pyajks.middlewares.PyajksDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'pyajks.pipelines.PyajksPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
