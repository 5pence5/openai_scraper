#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data

# Run the Scrapy spider
cd openai_scraper
scrapy crawl openai
