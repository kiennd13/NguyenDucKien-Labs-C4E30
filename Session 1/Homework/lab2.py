import requests
import re
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
a = soup.find_all("h3",limit=100)
ds=[]
for v in a :
    b = v.a.text
    ds.append(b)
# print(ds)
m = soup.find_all("h4",limit=100)
ds_singer =[]
for v in m:
    n = v.a.text
    ds_singer.append(n)
# print(ds[22])
# print(ds_singer)
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
df = pd.DataFrame({"Song":ds,"Singer":ds_singer})
writer = ExcelWriter("song_singer_top100_itunes.xlsx")
df.to_excel(writer,"Sheet1",index=False)
writer.save()


from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download([str(ds[22])+"-"+str(ds_singer[22])])
