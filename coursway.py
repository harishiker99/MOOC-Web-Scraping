from flask import Flask, flash, redirect, url_for
from flask import render_template, request
from bs4 import BeautifulSoup
import requests, lxml
import re
import sqlite3


app =Flask(__name__)




@app.route('/')
def home():

    return render_template("blank.html")
@app.route('/search',methods=['GET','POST'])
def search():
    if(request.method=='POST'):
        src_input=request.form['searche']
        conn = sqlite3.connect('scrap.db')
        curs = conn.cursor()
        curs.execute("DELETE from Coursera" )

        #print("Coursera")
        pre_url = "https://www.coursera.org"
        coursera_url = "https://www.coursera.org/courses?query={}&".format(src_input)
        src_source = requests.get(coursera_url).text
        soup = BeautifulSoup(src_source, 'lxml')
        product = soup.find_all('div', class_="ais-InfiniteHits")
        for x in product:
            test = x.find_all('li', class_="ais-InfiniteHits-item")
            for y in test:
                heade = y.h2.text
                imglink = y.img['src']
                review = y.span.text
                pro = y.a['href']
                price = "Not specified"
                pro = pre_url + pro
                curs.execute("insert into Coursera(head,link,price,review,imglink) values (?,?,?,?,?);",(heade,pro,price,review,imglink))

                #brand1 = curs.fetchall()
                conn.commit()
                #print(pro)
                #print(heade)
                #print(imglink)
                #print(review)
                #print("Cost- " + price)
        curs.execute("select * from Coursera")
        brand1=curs.fetchall()

        #print("Future Learn")
        pre_urlf = "https://www.futurelearn.com"
        edx_url = 'https://www.futurelearn.com/search?q={}'.format(src_input)
        src_esource = requests.get(edx_url).text
        soupu = BeautifulSoup(src_esource, 'lxml')
        #print("----------------------------------------------------------------------------")
        eproduct = soupu.find_all('li', class_="m-link-list__item")
        conn = sqlite3.connect('scrap.db')
        curs = conn.cursor()
        curs.execute("DELETE from Future")
        for x in eproduct:
            prod = x.a['href']
            heade = x.h3.text
            price = "Free"
            prod = pre_urlf + prod
            curs.execute("insert into Future(head,link,price) values (?,?,?);",
                         (heade, prod, price))
            brand2=curs.fetchall()
            conn.commit()
            #print(prod)
            #print(heade)
            #print("Cost-" + price)
        curs.execute("select * from Future")
        brand2=curs.fetchall()
        #print("Vskils")
        preimg_link="https://www.vskills.in/certification/"
        edx_url = 'https://www.vskills.in/certification/index.php?route=product/search&search={}'.format(src_input)
        src_esource = requests.get(edx_url).text
        soupu = BeautifulSoup(src_esource, 'lxml')
        #print("----------------------------------------------------------------------------")
        eproduct = soupu.find_all('div', class_="product-layout col-lg-4 col-md-4 col-sm-6 col-xs-12")
        conn = sqlite3.connect('scrap.db')
        curs = conn.cursor()
        #deleting data set from dB Browser
        curs.execute("DELETE from Vskill")
        for x in eproduct:
            prod = x.a['href']
            imglink = x.img['src']
            imglink=preimg_link+imglink
            heade = x.h4.text
            price = x.p.text
            cost = re.findall(r'[R][\w].+[\w]+', price)
            price = cost[0]
            curs.execute("insert into Vskill(head,link,price,imglink) values (?,?,?,?);",
                         (heade, prod, price,imglink))
            brand3=curs.fetchall()

            conn.commit()
           #print(prod)
            #print(heade)
            #print(price)
            #print(imglink)
        curs.execute("select * from Vskill")
        brand3=curs.fetchall()
        return render_template('search.html', brand1=brand1, brand2=brand2, brand3=brand3)

    else:
        return render_template('search.html')


if __name__=='__main__':
    app.run(debug=True)


