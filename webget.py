def get_stonk_price():
    import urllib.request as res
    URL="https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=&selectType=&_=1643028509474"
    request=res.Request(URL, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    })
    with res.urlopen(request) as res:
        data=res.read().decode("utf-8")
    