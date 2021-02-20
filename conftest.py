#!/user/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import time
import pytest
import requests
import urllib3

from Base.requestEngine import start_run_case
from Project_Tools.File_Tools import *


def push_flow_ID():
    """得到播放文件的推流ID"""
    ip = Tools.read_conf_yaml_file()
    url = f"http://{ip}:8800/api/push/add"
    file_sql = "   SELECT * FROM Tbl_FilePath   "

    File_LuJin = Tools.mysql(ip, file_sql).fetchall()

    data = {
          "custompath": f"rtmp://127.0.0.1:1937/BS/{Tools.UUID()}",
          "tasks": [
            {
              "explain": "mv",
              "transtype": "FILE_A",
              "src": f"{File_LuJin[0][2]}" #  文件服务器播放路劲
            }
          ],
          "loop": 1
        }
    result = requests.post(url, json=data).text
    try:
        assert json.loads(result)["code"] == 1
        return json.loads(result)["id"], File_LuJin[0][1]
    except:
        return "获取播放文件的推流ID错误"


def Meet_Room_ID():
    data = {
        "Verify": {
            "ServiceID": "77d5f13aad94119760f369f48d6f0470",
            "TimeStamp": int(Tools.Time()),
            "Token": "string",
            "Type": 4
        },
        "Code": "Q1029",
        "Param": [
            {
                "Key": "VideoRation",
                "Value": "string",
                "Type": 1
            }
        ],
        "Data": "string"
    }

    url = f"https://{Tools.read_conf_yaml_file()}:8090/aio2/gateway/api/v1/gateway/Query"

    logging.captureWarnings(True)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    result = requests.post(url=url, json=data, verify=False)
    data = json.loads(result.text)
    decode = Tools.DecodeBase64(data["BaseData"])
    return int(decode[-9:-1])

if __name__ == "__main__":
    print(type(Meet_Room_ID()))

