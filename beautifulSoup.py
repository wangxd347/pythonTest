import requests
# from bs4 import BeautifulSoup        解析网页  pip3 install Beautifulsoup4
from pyquery import PyQuery

def get_data_pyquery():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    url = 'https://www.baidu.com/s?ie=UTF-8&wd=王旭东'
    strhtml = requests.get(url, headers=headers)
    # strhtml.raise_for_status()
    strhtml.encoding = "utf-8"
    doc = PyQuery(strhtml.text)
    data = doc('#content_left h3 a').items()
    for item in data:
        result = {
            'title': item.text(),
            'link': item.attr('href')
        }
        print(result )

# --------------使用bs4解析网页-----------------
# def get_data_bs4():
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#     url = 'https://www.baidu.com/s?ie=UTF-8&wd=王旭东'
#     strhtml = requests.get(url,headers=headers)
#     soup = BeautifulSoup(strhtml.text, 'lxml')
#     data = soup.select('h3.t > a')
#     for item in data:
#         result = {
#             'title': item.get_text(),
#             'link': item.get('href')
#         }
#         print(result)

if __name__=='__main__':
    # get_data_bs4()
    get_data_pyquery()