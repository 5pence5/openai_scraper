#!/bin/bash

#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data

# Print working directory for debugging
echo "Current directory: $(pwd)"
ls -la

# Run scrapy from the root directory
scrapy crawl openai -p openai_scraper
