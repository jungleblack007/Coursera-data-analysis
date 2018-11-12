import json
from urllib.request import urlopen, quote
import requests,csv
import pandas as pd
pd.set_option('display.max_columns', None)


def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '99flG4xrb8OrWR2fOGBfLxqB9DdkhC90'
    add = quote(address) 
    #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() 
    #将其他编码的字符串解码成unicode
    temp = json.loads(res) 
    #对json数据进行解析
    return temp

milu = pd.read_excel('miludistrbute.xlsx')
milu['lat'] = None
milu['lon'] = None

for i in range(0,len(milu.index)):

	if 'result' in getlnglat(milu.iloc[i][3]):
	    milu['lon'][i] = getlnglat(milu.iloc[i][3])['result']['location']['lng']
	    milu['lat'][i] = getlnglat(milu.iloc[i][3])['result']['location']['lat']
	    print(milu.iloc[i])
	else:
		continue

milu.to_excel('milu1.xlsx')
