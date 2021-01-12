from bs4 import BeautifulSoup
import lxml
import requests
import csv
def get_html(url):
    r = requests.get(url)
    return r.text

def get_links(html):
    soup = BeautifulSoup(html,'lxml')
    zagolovki = soup.find_all('div', class_='t f_medium')
    photos = soup.find_all('li')
    zag = []
    photo = []
    links = []
    all_ = [links, zag,photo]
    for i in zagolovki:
        b = i.find('a').find('span', class_='n').text
        all_[1].append(b)
        d = i.find('a').get('href')
        all_[0].append(d)
    for i in photos:
        try:
            x = i.find('div', class_='i').find('a').find('img').get('data-src')
            all_[2].append(x)
        except:
            pass

    # f = open('file1.txt', 'w')
    # f.write(str(photo))
    # print(photo)
    return all_


def main():
    # url = 'https://kaktus.media/?date=2020-12-05&lable=8&order=time#paginator'
    # url='https://kaktus.media/'
    url='https://kaktus.media/?date=2020-12-06&lable=8&order=main'
    all_links = get_links(get_html(url))
    return all_links
main()