import requests
from bs4 import BeautifulSoup as bs

def getSamsungPages(url):
    urls = []
    new_url = ''
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    pages = soup.find_all('div', class_ = 'listing__pagination')
    temp = str(pages)
    temp1 = temp.split('<li class="" data-page="2">')[1]
    temp2 = temp1.split('href=')[1]
    urls.append(temp2.split('>')[0])
    for u in urls:
        new_url = u.replace('"', '')
    urls.remove(urls[0])
    urls.append(new_url)
    temp2 = temp1.split('<li class="" data-page="3">')[1]
    temp3 = temp2.split('href="')[1]
    urls.append(temp3.split('">')[0])
    temp3 = temp2.split('<li class="" data-page="4">')[1]
    temp4 = temp3.split('href="')[1]
    urls.append(temp4.split('">')[0])
    return urls