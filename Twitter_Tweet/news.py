from bs4 import BeautifulSoup
import requests
from constant import news

class News:
    def __init__(self):
        self.response = requests.get(url=news)
        self.yc_news_page = self.response.text
        self.soup = BeautifulSoup(self.yc_news_page, "html.parser")

    def get_latest_article(self):
        self.article_text = []
        self.article_link = []
        self.article_tags = self.soup.find_all(name="span", class_="titleline")
        for article_tag in self.article_tags:
            self.article_text.append(article_tag.contents[0].getText())
            self.article_link.append(article_tag.contents[0].get("href"))
        self.article_upvotes = [int(score.getText().split()[0]) for score in self.soup.find_all(name="span", class_="score")]     

    def get_high_upvotes_article(self):
        max_upvotes = max(self.article_upvotes)
        max_count_index = self.article_upvotes.index(max_upvotes)
        article = self.article_text[max_count_index] + ' ' + self.article_link[max_count_index]
        return article
    