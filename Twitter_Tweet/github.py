from bs4 import BeautifulSoup
import requests
from constant import github
from lxml import etree

class Github:
    def __init__(self, post):
        self.url = github.replace("01",post)
        self.response = requests.get(url=self.url)
        self.github_page = self.response.text
        self.soup = BeautifulSoup(self.github_page, "html.parser")

    def get_latest_post(self, post):
        dom = etree.HTML(str(self.soup))
        self.heading = dom.xpath('///*[@id="readme"]/article/h1/text()')[0]
        self.gif_link = self.soup.find(name="img", attrs={"alt": f'day{post}'}).get('src')
        print(self.heading)
        print(self.gif_link)
        return f"#100daysofcoding\n{self.heading}\n{self.gif_link}"
