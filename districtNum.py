import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import csv
from math import * 


if __name__ == "__main__":
    districts = ["chaoyang", "haidian", "fengtai", "shijingshan", "tongzhou", "changping", "daxing", "yizhuangkaifaqu", "shunyi", "fangshan", "mentougou", "pinggu", "huairou", "miyun", "yanqing", "yanjiao"]
    url1 = '''https://bj.lianjia.com/xiaoqu/rs'''
    url2 = '''https://lf.lianjia.com/xiaoqu/'''
    # url1 = 'http://restapi.amap.com/v3/place/text?keywords='
    # url2 = '&city=beijing&output=json&offset=20&page=1&key=5b47dc0e96645c177edf8fedaddc1e97&extensions=all'
    path = "/media/fuxihao/Data/MyWorkingDir/crawls/csv/"
    # path = '''D:\MyWorkingDir\crawls\csv\\'''

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    for district in districts:
        with open(path+district+'.csv', 'r', encoding='utf-8') as csvfile:
            with open(path+district+'_Num.csv', 'w', encoding='utf-8') as write:
                f_csv = csv.reader(csvfile)
                for row in f_csv:
                    name = row[0].split(' ')[0]
                    url = url1+name+'/'
                    try:
                        req = session.get(url)
                        soup = BeautifulSoup(req.text)
                        results = soup.find_all(class_="clear xiaoquListItem")
                    except:
                        results = []
                    # print(name)
                    num = 0
                    if (len(results) > 0):
                        result = results[0]
                        newUrl = url2+result['data-id']+'/'
                        r = session.get(newUrl)
                        s = BeautifulSoup(r.text)
                        
                        res = s.find_all(class_="xiaoquInfoContent")
                        # res = res.find_all(class_="xiaoquInfo")
                        for re in res:
                            tex = re.contents
                            if len(tex) > 0:
                                tex = tex[0]
                            else:
                                break
                            ind = tex.find('户')
                            if ind != -1:
                                
                                num = tex[:ind]
                                break
                    # print(num)
                    
                    spamwriter = csv.writer(write, delimiter=' ')
                    
                    spamwriter.writerow([name,num])
                print('yi ken la chya ku')