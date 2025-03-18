from bs4 import BeautifulSoup

from ..base import SimpleScraper


class NBC(SimpleScraper):
    def __init__(self, source_id):
        super().__init__(
            source_id=source_id, url="https://www.nbcnews.com/latest-stories/"
        )

    def parse_soup(self, soup: BeautifulSoup):
        news_list = []
        for news in soup.find_all(
            class_="wide-tease-item__wrapper df flex-column flex-row-m flex-nowrap-m"
        ):
            tag = news.find(class_="wide-tease-item__headline")
            url = tag.parent["href"]
            title = tag.text.strip()
            news_list.append({"url": url, "title": title})
        return news_list
