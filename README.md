# Web Crawlers 

The purpose of this project is to familiarize yourself with web crawlers and linguistic analysis of content. The project consists of multiple interdependent parts.

## Part 1: Web Crawler

In this part, we will write a program to retrieve and analyze the content of web pages.

### 1. Crawler

(a) Write a program that fetches the global gold price from a reliable website, such as Metal LME, and stores it in ElasticSearch. The method of setting up ElasticSearch is not important for this exercise, and you can even use its free cloud version. Only save the table with up to 12-month contracts.

Point 2: Schema design suitable for storage will be important and evaluated in all parts of the exercise.

(b) Obtain and save the price of active coins in the Iran Commodity Exchange market. Extract and store the fields inside the green rectangle from the page related to coins on the tsetmc site.

Tips: For web crawling, Python libraries such as Selenium, httplib, urllib, or requests are recommended. The BeautifulSoup library is recommended for content processing.

;
## Part 2: RSS Crawler

In this part, we will write a crawler based on RSS to extract news related to gold from the Kitco website.

### 2. RSS Crawler

Write a program that extracts gold-related news (along with related information) from the Kitco website's RSS feed. The RSS feed URL is http://news.kitco.com/rss. Filter the news and save them in the ElasticSearch database.

## Part 3: Persian Text Cleaning

In this part, we will focus on cleaning Persian texts and extracting specific items from them.

### 3. Cleaning Persian Texts

The goal here is to extract specific items from Persian texts stored in ElasticSearch.

(a) Extract hashtags from the text.
(b) Extract links from the text.
(c) Extract mentions from the text.
(d) Extract English words and phrases from the text.

Store all the extracted data in a new index in ElasticSearch. This information can be useful for various analyses.

Tips: You can use the re library for regular expressions.

## Part 4: Persian Text Analysis

In this part, we will use the Hazm library to analyze Persian texts stored in ElasticSearch.

### 4. Persian Text Analysis

Analyze the Persian data in ElasticSearch using the Hazm library. Apply the following steps to the data:

(a) Normalize the cleaned data.
(b) Tokenize the sentences in each text.
(c) Tokenize the words in each sentence.
(d) Stem the words.
(e) Label the words (verbs, adjectives, nouns, etc.).

In addition to presenting the results in the report file, store the extracted information from steps (c) to (e) in separate indexes in ElasticSearch. Explain how and why you chose the indexes in your report.

## Conclusion

This exercise introduces web crawlers and linguistic analysis of content. It guides you through the process of crawling web pages, extracting relevant data, cleaning Persian texts, and analyzing them using the Hazm library. Follow the instructions for each part and document your findings in a report. Enjoy exploring web content and analyzing Persian texts!
