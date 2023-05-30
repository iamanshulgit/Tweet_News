import requests
from constant import NEWSAPI, NEWS_ENDPOINT, QUERY

class NewsAPI:
    def __init__(self):
        self.params = {"apikey": NEWSAPI, "qInTitle": QUERY}
        self.response = requests.get(NEWS_ENDPOINT, self.params)
        self.all_articles = self.response.json()["articles"]
    
    def get_article(self, idx):
        article = self.all_articles[idx]
        content = f"#AI #news\n{article['title']}\n{article['url']}\n{article['urlToImage']}"
        return content
    