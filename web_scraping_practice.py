# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import requests

# req = Request('https://www.hellenicshippingnews.com/tag/top-stories/', headers={'User-Agent': 'Mozilla/5.0'})
# html = urlopen(req).read()
# soup = BeautifulSoup(html, 'html5lib')

# with requests.Session() as c:
#     soup = BeautifulSoup(html, 'html5lib')
#     for item in soup.find_all('div', attrs={'class': 'kCrYT'}):
#         raw_link = (item.find('a', href=True)['href'])
#         link = (raw_link.split('/url?q=')[1]).split('&sa=U&ved')[0]
#         print(link)

# raw_p_tags = []
# n=1
# for items in soup.find_all('p'):
#     raw_p_tags.append(items.get_text())


# brief = raw_p_tags[1::2]
# lucky = brief[n]
# # print(brief)
# print(lucky)
