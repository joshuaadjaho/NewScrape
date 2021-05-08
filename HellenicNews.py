from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import webbrowser


req_1 = Request('https://www.hellenicshippingnews.com/tag/top-stories/', headers={'User-Agent': 'Mozilla/5.0'})
req_2 = Request('https://www.tradewindsnews.com', headers={'User-Agent': 'Mozilla/5.0'})
hellenic_page_html = urlopen(req_1).read()
tradewinds_page_html = urlopen(req_2).read()
raw_p_tags = []
hellenic_headline_title_soup = BeautifulSoup(hellenic_page_html, 'html5lib')
article_number=0
news_array = [] 

# creating a class to store article information in
class news:
    def __init__(self, article_link, article_headline, article_description, source):
        self.article_link = article_link
        self.article_headline = article_headline
        self.article_description = article_description
        self.source = source 


# the brief content on hellenic shipping homepage
for items in hellenic_headline_title_soup.find_all('p'):
    raw_p_tags.append(items.get_text())

hellenic_summary = raw_p_tags[1::2]

# Hellenic shipping news
# extract the headline and link to the article
with requests.Session() as c:
    hellenic_headline_title_soup = BeautifulSoup(hellenic_page_html, 'html.parser')
    for item in hellenic_headline_title_soup.find_all('article', attrs={'class': 'item-list'}):
        hellenic_article_link = item.find('a', href=True)['href']
        hellenic_article_headline = item.find('a')['title'].split('Permalink to ')[1]
        hellenic_first_paragraph = hellenic_summary[article_number]
        news_array.append(news(hellenic_article_link, hellenic_article_headline, hellenic_first_paragraph, 'Hellenic Shipping News'))
        article_number +=1

# tradewinds news
with requests.Session() as c:
    tradewinds_headline_title_soup = BeautifulSoup(tradewinds_page_html, 'html.parser')
    for item in tradewinds_headline_title_soup.find_all('li', attrs={'class': 'p-2'}):
        tradewinds_article_link = item.find('a', href=True)['href']
        tradewinds_article_headline = item.find('a').get_text()
        req_3 = Request(str(tradewinds_article_link), headers={'User-Agent': 'Mozilla/5.0'})
        tradewinds_article_page_html = urlopen(req_3).read()
        tradewinds_article_page_soup = BeautifulSoup(tradewinds_article_page_html, 'html.parser')
        tradewinds_article_subtitle = tradewinds_article_page_soup.find('p')
        tradewinds_first_paragraph = tradewinds_article_page_soup.find_all('p')[1].get_text()
        news_array.append(news(tradewinds_article_link, tradewinds_article_headline, tradewinds_first_paragraph, 'Tradewinds'))


f=open('Shippingnews.html', 'w')

page_html_code = """
<body>

<div class="row">
    <div class="col s12 m6">
      <div class="card blue-grey darken-1">
        <div class="card-content white-text">
          <span class="card-title">Card Title</span>
          <p>I am a very simple card. I am good at containing small bits of information.
          I am convenient because I require little markup to use effectively.</p>
        </div>
        <div class="card-action">
          <a href="#">This is a link</a>
          <a href="#">This is a link</a>
        </div>
      </div>
    </div>
  </div>
            

<head></head>
<h1>%s</h1>
<p>
    %s
</p>
<p> 
    <em>read more at </em>
    <a href= %s target="_blank"><em>%s</em></a>
</p>
"""

page_html_code_1 = """
<h1>%s</h1>
<p>
    %s
</p>
<p> 
    <em>read more at </em>
    <a href= %s target="_blank"><em>Article</em></a>
</p>
"""

content = page_html_code*2

content_1 = content % (str(news_array[0].article_headline), str(news_array[0].article_description), str(news_array[0].article_link), str(news_array[0].source),
str(news_array[1].article_headline), str(news_array[1].article_description), str(news_array[1].article_link), str(news_array[1].source))

f.write()
f.close()

filename = 'file:///Users/joshadjaho/Desktop/Python work/Shippingnews.html'
webbrowser.open_new_tab(filename)