import scrapy
import os
import json
from datetime import datetime

class OpenAISpider(scrapy.Spider):
    name = "openai"
    allowed_domains = ["openai.com", "help.openai.com", "platform.openai.com"]
    start_urls = [
        "https://openai.com/",
        "https://help.openai.com/",
        "https://platform.openai.com/docs/"
    ]
    
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'OpenAI-Scraper (+https://github.com/yourusername/openai-scraper)',
    }
    
    def parse(self, response):
        # Store the page content
        url_path = response.url.replace("https://", "").replace("http://", "")
        filename = url_path.replace("/", "-").rstrip("-")
        if not filename:
            filename = "index"
            
        # Create directory structure
        output_dir = "data/" + datetime.now().strftime("%Y-%m-%d")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Save the HTML content
        with open(f"{output_dir}/{filename}.html", "wb") as f:
            f.write(response.body)
            
        # Extract metadata for easier tracking
        title = response.css("title::text").get()
        metadata = {
            "url": response.url,
            "title": title,
            "scrape_time": datetime.now().isoformat(),
            "content_length": len(response.body)
        }
        
        with open(f"{output_dir}/{filename}.meta.json", "w") as f:
            json.dump(metadata, f, indent=2)
        
        # Follow all links within the allowed domains
        for href in response.css("a::attr(href)"):
            yield response.follow(href, self.parse)
