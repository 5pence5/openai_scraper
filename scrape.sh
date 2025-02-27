#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data

# Debug information
echo "Current directory: $(pwd)"
ls -la

# List available spiders to help debug
echo "Available spiders:"
scrapy list

# Run the Scrapy spider with specific name
scrapy crawl openai
