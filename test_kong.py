#!/user/bin/env python
# -*- coding: utf-8 -*-
import logging

import requests
import urllib3

from Base.requestEngine import start_run_case
from Live_data import Main_Function_Test_Suite_Data as data_class
from Project_Tools.File_Tools import Tools

class Test:

    def test(self):
        data = {
        "Verify": {
          "ServiceID": "383d8698ccc6bc3390a13c925b5a180f",
          "Token": "token",
          "TimeStamp": Tools.Time(),
          "Type": 4
        },
        "Code": "M1006",
        "Param": [
        {
          "Key": "TskGuid",
          "Value": "0527dc0d1e0f4d5bafa17571e2245bf6",
          "Type": 2
        }
        ],
        "Data": ""
      }
        logging.captureWarnings(True)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url = "https://192.168.5.181:8090/aio2/gateway/api/v1/gateway/Business"
        result = requests.post(url, json=data, verify=False)
        print(result.text)