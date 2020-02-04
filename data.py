# Author: Autumnhui

import time,requests,json

# 数据获取
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)

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

# 有病例国家列表
country_list =[]
for i in world_data:
    country_list.append(i['name'])
print('有病例国家列表',country_list)

# 各国家数目
country_num_list =[]
for i in world_data:
    country_num_list.append(i['total']['confirm'])
print('各国家数目',country_num_list)

# 中国地区总列表
china_list = [world_data[0]['children']]
print('中国地区总列表',china_list)

# 中国各省份列表
china_province_list = []
for i in china_list[0]:
    china_province_list.append(i['name'])
print('中国各省份列表',china_province_list)

# 中国各省份病例数目列表
china_province_num_list = []
for i in china_list[0]:
    china_province_num_list.append(i['total']['confirm'])
print('中国各省份病例数目列表',china_province_num_list)




# for i in len(data['areaTree']):
#     place = data['areaTree']['name']
#     print(place)

# confirm_list = list()
# for item in data:

# data.sort(key=lambda x: x['date'])

# date_list = list()  # 日期
# confirm_list = list()  # 确诊
# suspect_list = list()  # 疑似
# dead_list = list()  # 死亡
# heal_list = list()  # 治愈
# for item in data:
    # month, day = item['date'].split('.')
    # date_list.append(datetime.strptime('2020-%s-%s' % (month, day), '%Y-%m-%d'))
    # confirm_list.append(int(item['confirm']))
    # suspect_list.append(int(item['suspect']))
    # dead_list.append(int(item['dead']))
    # heal_list.append(int(item['heal']))
