from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

req_2 = Request('https://www.tradewindsnews.com', headers={'User-Agent': 'Mozilla/5.0'})
tradewinds_page_html = urlopen(req_2).read()

# tradewinds news
with requests.Session() as c:
    headline_title_soup = BeautifulSoup(tradewinds_page_html, 'html.parser')
    for item in headline_title_soup.find_all('li', attrs={'class': 'p-2'}):
        Tradewinds_link = item.find('a', href=True)['href']
        headline = item.find('a').get_text()
        req_3 = Request(str(Tradewinds_link), headers={'User-Agent': 'Mozilla/5.0'})
        article_page_html = urlopen(req_3).read()
        article_page_soup = BeautifulSoup(article_page_html, 'html.parser')
        article_subtitle = article_page_soup.find('p')
        first_paragraph = article_page_soup.find_all('p')[1].get_text()
        print(first_paragraph)

