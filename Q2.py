import feedparser
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

d = feedparser.parse('https://news.kitco.com/rss/')

num=0
for entry in d.entries:

  if 'Gold'in entry.title or 'gold' in entry.title:
       print(entry.title)
       print(entry.link)
       print(entry.published)
       num+=1

       doc = {'Title': entry.title,'link':str(entry.link),'Date':entry.published,'Description':entry.description}

       resp = es.index(index="q2", id=num, document=doc)
       print(resp['result'])