#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas
from to_csv import mongo_to_csv

if __name__=='__main__':

    mongo_to_csv()

    target=pandas.read_csv('zhihu_user_data_30k.csv',encoding='utf-8')
    city_count=target[u'所在地'].value_counts()[:10]

    plt=city_count.plot(kind='bar',title="City Statistics").get_figure()
    plt.savefig("city.png")




