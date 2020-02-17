# 2019-nCov_dataAnalysis
 用Python语言通过腾讯新闻获取并整理关于武汉肺炎相关人数数据进行学习。

[![GitHub forks](https://img.shields.io/github/forks/Autumnhui/2019-nCov_dataAnalysis?style=social)](https://github.com/Autumnhui/2019-nCov_dataAnalysis/network/members)        [![GitHub stars](https://img.shields.io/github/stars/Autumnhui/2019-nCov_dataAnalysis?style=social)](https://github.com/Autumnhui/2019-nCov_dataAnalysis/stargazers)

## 🥩原始数据
![原始数据](./pic/raw-data.png) *数据来源：https://news.qq.com/zt2020/page/feiyan.htm*

## 🔧数据处理

通过对收集数据转为列表，再进行对列表/字典的操作取出相关值（数目/地区/时间），然后再赋值输出到对应列表。


![数据处理](./pic/屏幕快照%202020-02-16%20下午9.31.34.png)

## 📡Flask网页展示

使用Flask/Jinja2功能进行数据传输到网页端进行展示。

![flask](./pic/屏幕快照%202020-02-16%20下午9.43.12.png)
