from bs4 import BeautifulSoup
import urllib.request
from itertools import zip_longest, product


class Product:
    def __init__(self, name, price, img_url):
        self.name = name
        self.price = price
        self.img_url = img_url

    def show(self):
        print(f"{self.name} | {self.price} | {self.img_url}")

def request():
    hdr = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
    for n in range(1, 3):
        data = 'https://labgolfkorea.com/product/list.html?cate_no=55&page=' + str(n)
        #print('접속 URL:', data)
        req = urllib.request.Request(data, headers=hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        items = soup.select('li.xans-record-')  # 상품 하나 단위 (사이트 구조 따라 다름)
        datalist = []

        for item in items:
            try:
                name = item.select_one('p.name')
                price = item.select_one('p.price')
                img_tag = item.select_one('.thumbnail img')
                imgPath = img_tag.get('src') if img_tag else 'no Image'

                title = name.get_text(strip=True) if name else 'unknown'
                price_text = price.get_text(strip=True)
                product = Product(title, price_text, imgPath)
                datalist.append(product)
            except:
                pass

        for data in datalist:
            data.show()
            #print(data.name, data.price, data.img_url)


if __name__ == "__main__":
    request()
