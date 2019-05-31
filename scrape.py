from bs4 import BeautifulSoup
import requests, lxml
import re
import time


src_input=input("Enter the course you want to learn")

print("Coursera")
pre_url="https://www.coursera.org"
coursera_url="https://www.coursera.org/courses?query={}&".format(src_input)
src_source= requests.get(coursera_url).text
soup=BeautifulSoup(src_source,'lxml')
product=soup.find_all('div',class_="ais-InfiniteHits")
for x in product:
    test=x.find_all('li',class_="ais-InfiniteHits-item")
    for y in test:
        heade=y.h2.text
        imglink=y.img['src']
        review= y.span.text
        pro=y.a['href']
        price="Not specified"
        pro=pre_url+pro
        print(pro)
        print(heade)
        print(imglink)
        print(review)
        print("Cost- "+price)

        

print("Future Learn")
pre_urlf="https://www.futurelearn.com"
edx_url='https://www.futurelearn.com/search?q={}'.format(src_input)
src_esource = requests.get(edx_url).text
soupu=BeautifulSoup(src_esource,'lxml')
print("----------------------------------------------------------------------------")
eproduct=soupu.find_all('li',class_="m-link-list__item")
for x in eproduct:
    prod=x.a['href']
    heade=x.h3.text
    price="Free"
    prod=pre_urlf+prod
    print(prod)
    print(heade)
    print("Cost-"+price)





print("Vskils")

edx_url='https://www.vskills.in/certification/index.php?route=product/search&search={}'.format(src_input)
src_esource = requests.get(edx_url).text
soupu=BeautifulSoup(src_esource,'lxml')
print("----------------------------------------------------------------------------")
eproduct=soupu.find_all('div',class_="product-layout col-lg-4 col-md-4 col-sm-6 col-xs-12")
for x in eproduct:
    prod=x.a['href']
    imglink=x.img['src']
    heade=x.h4.text
    price=x.p.text
    cost=re.findall(r'[R][\w].+[\w]+', price)
    price=cost[0]
    print(prod)
    print(heade)
    print(price)
    print(imglink)
