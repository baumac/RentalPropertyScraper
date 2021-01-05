# Rental Property Scraper 

## Description
This Python app uses Selenium Webdriver to scrape property listings from real estate websites. 
The app gathers the listing price, annual rental income, and url to the listing and then stores it in a csv file. 

### Technology used
1. Python - the programming language
2. Selenium Webdriver - to scrape the web pages
3. Docker - to provide a stable runtime environment

### Supported websites: 
1. Redfin
---

## Usage

#### Note: make sure to update the config.yaml file located in the project root

The application has two ways to build and run it in a docker container:
1. Using a run script
2. Manually running it using docker
3. Running it locally with Python3

### Run Script Usage:
From the project root you can run any of these commands:
- ./run buildApp - Builds the application's docker container and tags it as rental_property_scraper:latest.
- ./run runApp - Runs the application's docker container.
- ./run buildAndRunApp - Builds and then runs the application's docker container.

### Manual Docker Usage:
From the project root run the following commands in order:
1. `docker build -t rental_property_scraper:latest -f Dockerfile .` - build the application docker container
2. `docker run rental_property_scraper:latest` - run the docker container

### Local usage with Python3:
1. pip install -r requirements.txt
2. python3 main.py