BOT_NAME = "openai_scraper"

SPIDER_MODULES = ["openai_scraper.spiders"]
NEWSPIDER_MODULE = "openai_scraper.spiders"

# Crawl responsibly by identifying yourself on the user agent
USER_AGENT = "OpenAI-Scraper (+https://github.com/yourusername/openai-scraper)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1

# Disable cookies
COOKIES_ENABLED = False

# Configure item pipelines
ITEM_PIPELINES = {}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Limit crawl depth to prevent infinite crawling
DEPTH_LIMIT = 5
