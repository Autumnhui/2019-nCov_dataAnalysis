# Author: Autumnhui
from flask import Flask,render_template,request
import time,requests,json

# 数据获取
## 人数数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)
# 新闻数据
# url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_time_line&callback=&_=%25d'%int(time.time()*1000)
# news_data = json.loads(requests.get(url=url).json()['data'])
# print(news_data)

# # 新闻时间
# news_time=[]
# for i in news_data:
#     news_time.append(i['time'])
# print(news_time)
# # 新闻标题
# news_title=[]
# for i in news_data:
#     news_title.append(i['title'])
# print(news_title)
# # 新闻内容
# news_desc=[]
# for i in news_data:
#     news_desc.append(i['desc'])
# print(news_desc)
# #新闻来源
# news_source=[]
# for i in news_data:
#     news_source.append(i['source'])
# print(news_source)

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



app = Flask(__name__)

@app.route('/')
def entry():
    time1=time #数据时间
    data1=confirm_total_china # 中国确诊人数
    data2=suspect_total_china # 中国疑似人数
    data3=dead_total_china # 中国死亡人数
    data4=heal_total_china # 中国治愈人数
    place1=country_list # 发现病例国家列表
    place2= china_province_list # 中国存在病例省份列表
    place3=china_city_list # 中国存在病例城市列表
    num1= country_num_list # 各国家数目
    num2= china_province_confirm_num_list # 中国各省份病例数目
    num3=china_province_dead_num_list # 中国各省份死亡数目列表
    num4=china_province_heal_num_list # 中国各省份治愈数目列表
    num5=china_city_confirm_num_list #各省份城市确诊数目列表
    num6=china_city_dead_num_list #各省份城市死亡数目列表
    num7=china_city_heal_num_list #各省份城市治愈数目列表
    return render_template('show_data.html',
                           time=time1,
                           confirm_total_china=data1,
                           suspect_total_china=data2,
                           dead_total_china=data3,
                           heal_total_china=data4,
                           country_list=place1,
                           china_province_list=place2,
                           china_city_list=place3,
                           country_num_list=num1,
                           china_province_confirm_num_list=num2,
                           china_province_dead_num_list=num3,
                           china_province_heal_num_list=num4,
                           china_city_confirm_num_list=num5,
                           china_city_dead_num_list=num6,
                           china_city_heal_num_list=num7)

if __name__ == '__main__':
    app.run()
