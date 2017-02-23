# -*- encoding: utf-8 -*-
#运营商首次授权初始化请求签名字典
dic_init = {"service_type": "transportation",
       "timestamp": "1468569870111l",
       "source": "100000",
       "client_customer_id": "",
       "account" : ""}
#运营商结果查询请求签名字典
dic_result = {"service_type": "transportation",
       "timestamp": "1468569870111l",
       "source": "100000",
       "client_customer_id": "",
       "data_format_type" : "origin",
       "account" : ""}
#授权初始化地址
init_url = "https://open.cafintech.com/auth/transportation/api/v2/init/10000/%s?source=10000&type=repot&customer_id=%s&turn_net=&operator=&signature=%s&timestamp=1468569870111&name=lizhen"

#获取授权结果接口
result_url = "http://54.222.193.152:9000/platform/query/v1/100000?service_type=transportation&data_format_type=origin&account=%s&timestamp=1468569870111&signature=%s"