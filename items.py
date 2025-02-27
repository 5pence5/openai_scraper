import scrapy

class OpenaiScraperItem(scrapy.Item):
    # Define the fields for your item here:
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    timestamp = scrapy.Field()
