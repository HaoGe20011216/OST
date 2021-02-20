#!/user/bin/env python
# -*- coding: utf-8 -*-
import base64
import io
import random
import re
import time
import uuid
import pymysql
import hashlib  # md5加密
import yaml


class Tools():

    @staticmethod
    def md5(str):
        md5 = hashlib.md5()
        md5.update(str.encode("utf-8"))  # 编码设置
        return md5.hexdigest()  # 返回16进制消息摘要

    @staticmethod
    def Ebase64(string):
      return str(base64.b64encode(string.encode('utf-8')), 'utf-8')  # 返回字符串类型

    @staticmethod
    def DecodeBase64(data):
        return str(base64.b64decode(data).decode("utf-8"))

    @staticmethod
    def Time():
        return int(time.time())

    @staticmethod
    def UUID():
        s_uuid = str(uuid.uuid4())
        l_uuid = s_uuid.split('-') # 抽离
        s_uuid = ''.join(l_uuid) # 合并
        return str(s_uuid)

    @staticmethod
    def number():
        return random.randint(1, 10000)

    @staticmethod
    def read_conf_yaml_file():
        with open(r"C:\Users\30420\PycharmProjects\OST\Conf\conf.yml", 'r', encoding='utf-8') as f:
            yaml_info = yaml.safe_load(f)
            s = re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])",
                          yaml_info["server_info"]["base_url"])[0]
            return str(s)

    @staticmethod
    def mysql(host, sql):
        connsql = pymysql.Connect(host=host, port=23306, user="root", database="AIO2", password="kunlun2020",
                                  charset="utf8")
        lv = connsql.cursor()  # 科涩
        lv.execute(sql)  # a死q的
        lv.close()
        connsql.close()
        return lv

    @staticmethod
    def result_data_file(result_data):
        with io.open(r"C:\Users\30420\PycharmProjects\OST\result_data_file.json", "w", encoding="utf-8") as result:
            result.write(result_data)
            return "<---------------数据写入成功，请到 result_data_file.json 文件查看结果--------------->"


if __name__ == "__main__":
    # "   select Fld_User_Guid, Fld_User_Name FROM Tbl_TerminalInfo WHERE Fld_User_Name LIKE 'www%'  "
    s = Tools.mysql(Tools.read_conf_yaml_file(), "   select Fld_User_Guid, Fld_User_Name FROM Tbl_TerminalInfo WHERE Fld_User_Name LIKE 'www%'  ")
    print(s.fetchall())











