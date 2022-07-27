def fb():
    import requests as rq
    from bs4 import BeautifulSoup as bs
    url = "https://www.cnbc.com/quotes/FB-IT"
    r = rq.get(url)
    soup = bs(r.content,"html.parser")
    price = soup.find("span",{"class":"QuoteStrip-lastPrice"})

    return price.text
