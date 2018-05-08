import requests
import json
import csv
# "116.603039,40.080525", 首都机场
# "116.412505,39.542600", 大兴机场
from math import * 
  
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """  
    # 将十进制度数转化为弧度  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
    # haversine公式  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 # 地球平均半径，单位为公里  
    return c * r * 1000  

def calcDistance(Lng_A, Lat_A, Lng_B, Lat_B):  
    '输入两点的经纬度计算两者距离'  
    ra = 6378.140  # 赤道半径 (km)  
    rb = 6356.755  # 极半径 (km)  
    flatten = (ra - rb) / ra  # 地球扁率  
    rad_lat_A = radians(Lat_A)  
    rad_lng_A = radians(Lng_A)  
    rad_lat_B = radians(Lat_B)  
    rad_lng_B = radians(Lng_B)  
    pA = atan(rb / ra * tan(rad_lat_A))  
    pB = atan(rb / ra * tan(rad_lat_B))  
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))  
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2  
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2  
    dr = flatten / 8 * (c1 - c2)  
    distance = ra * (xx + dr)  
    return distance 

def dis(lng1, lat1, lng2, lat2):
    pi = 3.14159265359
    R = 6370996.81
    Distance = R*acos(cos(lat1*pi/180 )*cos(lat2*pi/180)*cos(lng1*pi/180 -lng2*pi/180)+sin(lat1*pi/180 )*sin(lat2*pi/180)) 

    return Distance
if __name__ == "__main__":
    districts = ["dongcheng", "xicheng", "chaoyang", "haidian", "fengtai", "shijingshan", "tongzhou", "changping", "daxing", "yizhuangkaifaqu", "shunyi", "fangshan", "mentougou", "pinggu", "huairou", "miyun", "yanqing", "yanjiao"]
    url1 = 'http://restapi.amap.com/v3/place/text?keywords='
    url2 = '&city=beijing&output=json&offset=20&page=1&key=5b47dc0e96645c177edf8fedaddc1e97&extensions=all'
    # path = "/media/fuxihao/Data/MyWorkingDir/crawls/csv/"
    path = '''/csv/'''

    # longi_cap = 116.603039
    # lat_cap   = 40.080525
    # longi_daxing = 116.412505
    # lat_daxing   = 39.542600
    for district in districts:
        with open(path+district+'.csv', 'r', encoding='utf-8') as csvfile:
            with open(path+district+'_LogAndLat.csv', 'w', encoding='utf-8') as write:
                f_csv = csv.reader(csvfile)
                for row in f_csv:
                    name = row[0].split(' ')[0]
                    url = url1+name+url2
                    r = requests.get(url).json()['pois']
                    
                    if r!=[]:
                        r = r[0]['location']
                    
                        longi, lat = r.split(',')
                        longi = float(longi)
                        lat   = float(lat)
                        
                        # dis_cap = calcDistance(longi, lat, longi_cap, lat_cap)
                        # dis_daxing = calcDistance(longi, lat, longi_daxing, lat_daxing)
                        
                    else:    
                        longi = 0.0
                        lat = 0.0
                    spamwriter = csv.writer(write, delimiter=' ')
                    
                    spamwriter.writerow([name,longi, lat])
                    

               
                