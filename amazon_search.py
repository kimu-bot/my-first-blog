#使うツール
import requests     
import bs4         
from bs4 import BeautifulSoup

#ゲストにワード検索させたい
a = input('テキストを入力してください。：')
page_url = "https://www.amazon.co.jp/s?k=" + "(a)"

#価格を抜き取りたい
def get_price(page_url):
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    selected_html = soup.select('.a-span12 span.a-color-price')

    if not selected_html:
        selected_html = soup.select('.a-color-base span.a-color-price')

    pattern = r'\d*,?\d*,?\d*\d'
    regex = re.compile(pattern)
    matches = re.findall(regex, selected_html[0].text)
    price = matches[0].replace(',', '')
    return int(price)

#商品名を抜き取りたい
def get_title(page_url):
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    selected_html = soup.select('#productTitle')
    title = selected_html[0].text
    title = title.replace(' ', '')
    title = title.replace('\n', '')
    return title

#上位結果10個に絞り、書き込みたい
for i in range(10):
      a = str(list[i]).strip()
      result_title = title
      result_price = int(price)
      f.write('{0},{1}\n'.format(result_title, result_price))