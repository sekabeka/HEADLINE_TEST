from bs4 import BeautifulSoup

from ..base import SimpleScraper


class RIA(SimpleScraper):
    def __init__(self, source_id):
        super().__init__(source_id=source_id, url="https://ria.ru/lenta/")

    def parse_soup(self, soup: BeautifulSoup):
        news_list = []
        for news in soup.find_all(class_="list-item"):
            tag = news.find(class_="list-item__title")
            title = tag.text.strip()
            url = tag["href"]
            news_list.append({"url": url, "title": title})
        return news_list
