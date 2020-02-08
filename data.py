# Author: Autumnhui

import time,requests,json

# 数据获取
## 人数数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)
## 新闻数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_time_line&callback=&_=%25d'%int(time.time()*1000)
news_data = json.loads(requests.get(url=url).json()['data'])
print(news_data)

# 新闻时间
news_time=[]
# for i in news_data:
#     news_time.append(i['time'])
# print(news_time)
#
# # 新闻标题
news_title=[]
# for i in news_data:
#     news_title.append(i['title'])
# print(news_title)
news_time=[]
news_title=[]
news_desc=[]
news_source=[]
news=[]
news_all=[news_time,news_title,news_desc,news_source]
news_type=['time','title','desc','source']
for a in news_all:
    for b in news_type:
        for c in news_data:
            a.append(c[b])
print(news_desc)

# 创建列表
confirm_total_china = list()
suspect_total_china = list()
dead_total_china = list()
heal_total_china = list()

# 全国确诊人数
confirm_total_china.append(int(data['chinaTotal']['confirm']))
print('全国确诊人数：',confirm_total_china)
# 全国疑似人数
suspect_total_china.append(int(data['chinaTotal']['suspect']))
print('全国疑似人数：',suspect_total_china)
# 全国死亡人数
dead_total_china.append(int(data['chinaTotal']['dead']))
print('全国死亡人数：',dead_total_china)
# 全国治愈人数
heal_total_china.append(int(data['chinaTotal']['heal']))
print('全国治愈人数：',heal_total_china)
# 数据更新时间
time= data['lastUpdateTime']
print('数据更新时间：',time)

# 整体数据
world_data= data['areaTree']
# print(world_data)

# 发现病例国家列表
country_list =[]
for i in world_data:
    country_list.append(i['name'])
print('发现病例国家列表',country_list)

# 各国家存在病例数目
country_num_list =[]
for i in world_data:
    country_num_list.append(i['total']['confirm'])
print('各国家数目',country_num_list)

# 中国地区总列表
china_list = [world_data[0]['children']]
# print('中国地区总列表',china_list)

# 中国各省份列表
china_province_list = []
for i in china_list[0]:
    china_province_list.append(i['name'])
print('中国各省份列表',china_province_list)

# 中国各省份病例数目列表
china_province_confirm_num_list = []
for i in china_list[0]:
    china_province_confirm_num_list.append(i['total']['confirm'])
print('中国各省份确诊病例数目列表',china_province_confirm_num_list)

china_province_dead_num_list = []
for i in china_list[0]:
    china_province_dead_num_list.append(i['total']['dead'])
print('中国各省份死亡数目列表',china_province_dead_num_list)

china_province_heal_num_list = []
for i in china_list[0]:
    china_province_heal_num_list.append(i['total']['heal'])
print('中国各省份治愈数目列表',china_province_heal_num_list)


# 中国存在病例的所有城市列表-确诊，死亡，治愈
china_city0_list =[]
for i in china_list[0]:
    china_city0_list.append(i['children'])         # 列表嵌套列表（一个省份为一个列表）
china_city1_list=sum(china_city0_list,[])          # 将列表合并为一个列表，再进行取值
china_city_list=[]
for a in china_city1_list:
    china_city_list.append(a['name'])
print('各省份城市存在病例列表',china_city_list)

# 各省份城市确诊数目列表
china_city_confirm_num_list=[]
for a in china_city1_list:
    china_city_confirm_num_list.append(a['total']['confirm'])
print('各省份城市确诊数目列表',china_city_confirm_num_list)

# 各省份城市死亡数目列表
china_city_dead_num_list=[]
for a in china_city1_list:
    china_city_dead_num_list.append(a['total']['dead'])
print('各省份城市死亡数目列表',china_city_dead_num_list)

# 各省份城市治愈数目列表
china_city_heal_num_list=[]
for a in china_city1_list:
    china_city_heal_num_list.append(a['total']['heal'])
print('各省份城市治愈数目列表',china_city_heal_num_list)