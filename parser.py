import requests
from bs4 import BeautifulSoup
import time,json

headers = {
    "accept":"*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.54"
    }

def txt_update(txt):
    rep = [","," ","-","\'","/","\\"]
    gg = txt
    for item in rep:
        if item in txt:
            gg = txt.replace(item,"-")
    return gg

link = "https://www.auto-data.net"
url2 = "https://www.auto-data.net/ru/allbrands"
fn = [
]



def main():
    data = BeautifulSoup(requests.get(url=url2,headers=headers).text,"lxml")
    gsus = 1
    for i in data.find_all(class_="marki_blok"):
        da = {}
        name = txt_update(i.text)
        print(name)
        lin = link + i.find("img").get("src")
        da["name"]=i.text
        da["img"] = f"auto/{name}.jpg"
        fn.append(da)
        gsus += 1
    with open("cars.json","w",encoding="utf-8") as file:
        json.dump(fn, file,ensure_ascii=False,indent=4)
    print(fn)

main()
