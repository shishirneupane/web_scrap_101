# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_HTML_text(url):
    response = requests.get(url)
    responsepage = response.text
    response_status = response.status_code

    if response_status == 200:
        return responsepage
    elif response_status == 403:
        raise Exception("try after minute again")
    else:
        raise Exception("oops something went wrong")

#get html text of website
responsepage = get_HTML_text("https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht")
#parse html
responsepagesoup = BeautifulSoup(responsepage,"html.parser")
#select table
container = responsepagesoup.find("table",{"class":"chart full-width"})
#select table ko tbody ko tr
trs = container.find("tbody").findAll("tr")

# file create
try:
    f = open("movies.csv", "w")
    f.write("name, image \n")   # headers

    for tr in trs:
        title = tr.find("td",{"class","titleColumn"}).a.text
        image = tr.find("td",{"class","posterColumn"}).a.img["src"]
        f.write(title+",\""+image+"\"\n")

except Exception as e:
    print("oops exception occurs", e)

else:
    #file close
    f.close()

#element -> classname -> id -> data attribute
