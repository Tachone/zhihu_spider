# zhihu_spider
### 大规模知乎用户爬虫
* （１）使用python的request模块获取html页面，注意要修改自己的cookie，使得我们更像是使用浏览器访问
* （２）使用xpath模块从html中提取需要的关键信息（姓名，职业，居住地，关注人等）
* （３）使用redis作为队列，很好的解决并发和大规模数据的问题（可以分布式）
* （４）使用bfs宽度优先搜索，使得程序得以不断扩展持续搜索用户
* （５）数据存储至no-sql数据库：mongodb（高效轻量级并且支持并发）
* （６）使用python的进程池模块提高抓取速度
* （７）使用csv,pandas,matplotlib模块进行数据处理（需要完善）
    
### 联系作者
* 具体可以参考我的博客：http://blog.csdn.net/nk_test/article/details/51330971
* 运行的时候需要指定参数 ： print_data_out 表示输出至屏幕；store_data_to_mongo代表存入mongodb数据库
  同时依赖redis,mongodb以及python的部分模块，请自行安装。
     

### 数据展示：
![image](https://github.com/Tachone/zhihu_spider/blob/master/career.png)
![image](https://github.com/Tachone/zhihu_spider/blob/master/city.png)
![image](https://github.com/Tachone/zhihu_spider/blob/master/title.png)
