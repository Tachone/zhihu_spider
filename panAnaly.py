#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas
from to_csv import mongo_to_csv



import matplotlib.pyplot as mplt
if __name__=='__main__':

    #将数据库中的数据转化成csv格式
    mongo_to_csv()

    #使用pandas模块进行条形图的绘制；TODO 更加详细的分析
    target=pandas.read_csv('zhihu_user_data_30k.csv',encoding='utf-8')
    city_count=target[u'所在地'].value_counts()[:10]
   # plt=city_count.plot(kind='bar',title="City Statistics",figsize=(10,10)).get_figure()
    plt=city_count.plot(kind='barh',title="City Statistics").get_figure()
    mplt.legend(loc='best')
    plt.savefig("city.png")




