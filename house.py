#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import csv
# soup = BeautifulSoup(markup, "html5lib")

url = "https://bj.lianjia.com/xiaoqu/"




def get_data_of_a_dis(district):
    r = requests.get(url+district)
    # print(r.text)
    soup = BeautifulSoup(r.text)
    result = soup.find_all(class_="page-box house-lst-page-box")[0]
    totalPage = json.loads(result['page-data'])['totalPage']
    
    xiaoqus = {}   # 小区名：　价格

    for i in range(totalPage):
        newUrl = url+ district + '/pg' + str(i+1)
        newR = requests.get(newUrl)
        soup = BeautifulSoup(newR.text)
        results = soup.find_all(class_="clear xiaoquListItem")
        for result in results:
            price = result.find_all(class_="totalPrice")[0].span.contents[0]
            xiaoquming = result.find_all(class_="title")[0].a.contents[0]
            
            xiaoqus[xiaoquming] = price
    return xiaoqus
        
if __name__ == "__main__":
    
    districts = ["dongcheng", "xicheng", "chaoyang", "haidian", "fengtai", "shijingshan", "tongzhou", "changping", "daxing", "yizhuangkaifaqu", "shunyi", "fangshan", "mentougou", "pinggu", "huairou", "miyun", "yanqing", "yanjiao", "xianghe"]

    for district in districts:
        xiaoqus = get_data_of_a_dis(district)
        path = "csv/"
        with open(path+district+'.csv', 'w', newline='', encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for key in xiaoqus:
                print(key)
                spamwriter.writerow([key,xiaoqus[key]])
        
     

    