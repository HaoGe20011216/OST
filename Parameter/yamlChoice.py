#!/user/bin/env python
# -*- coding: utf-8 -*-
from opensourcetest.builtin.autoParamInjection import AutoInjection

class Main_Function_Test_Suite(AutoInjection):
    def __init__(self):
        super(Main_Function_Test_Suite, self).__init__("Main_Function_Test_Suite", "Main_Function_Test_Suite")

class Query_call_devices(AutoInjection):
    def __init__(self):
        super(Query_call_devices, self).__init__("query_call_devices", "query_call_devices")

if __name__ == '__main__':
    ...
