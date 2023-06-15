# Web Crawlers 

The purpose of this project is to familiarize yourself with web crawlers and linguistic analysis of content. The project consists of multiple interdependent parts.

## Part 1: Web Crawler

In this part, we will write a program to retrieve and analyze the content of web pages.

### 1. Crawler

(a) Write a program that fetches the global gold price from a reliable website, such as Metal LME, and stores it in ElasticSearch. The method of setting up ElasticSearch is not important for this exercise, and you can even use its free cloud version. Only save the table with up to 12-month contracts.

Point 2: Schema design suitable for storage will be important and evaluated in all parts of the exercise.

(b) Obtain and save the price of active coins in the Iran Commodity Exchange market. Extract and store the fields inside the green rectangle from the page related to coins on the tsetmc site.

Tips: For web crawling, Python libraries such as Selenium, httplib, urllib, or requests are recommended. The BeautifulSoup library is recommended for content processing.

## Part 2: RSS Crawler

In this part, we will write a crawler based on RSS to extract news related to gold from the Kitco website.

### 2. RSS Crawler

Write a program that extracts gold-related news (along with related information) from the Kitco website's RSS feed. The RSS feed URL is http://news.kitco.com/rss. Filter the news and save them in the ElasticSearch database.

### Conclusion
This exercise introduces web crawlers. It guides you through the process of crawling web pages, extracting relevant data.
