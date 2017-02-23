#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import bytes
import json,os
from jpype import *
#调用java函数时，最好是给String等基本类型，因为其他类型转换不对就很坑
'''
       多次调用时，会报错，无法启动第二个JVM，布吉岛是我的使用不对还是真的有问题，目前没查到解决办法！！！
'''
class Sig:
       def __init__(self):
              self.key = "CAF824-A19118-410B-8FED-AB38F600"
              self.jarpath = os.path.join(os.path.abspath('.')+'/sig_jar/li.jar')
       def get_signature(self,dic_data):
              startJVM(getDefaultJVMPath(), "-Djava.class.path=%s" % self.jarpath)
              self.jd = JPackage("com.li").EncryptionUtil
              #输出
              # jprint = java.lang.System.out.println
              # jprint(jd.generateSignature(json.dumps(dic_query),key))
              self.data = self.jd.generateSignature(json.dumps(dic_data),self.key)
              shutdownJVM()
              return self.data

