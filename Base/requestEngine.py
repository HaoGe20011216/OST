#!/user/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from typing import Text, Union

import urllib3
from opensourcetest.common.yamlOperation import YamlFileOption
from opensourcetest.builtin.ostHttp import ost_http_runner
# Read the conf.yml Global profile
conf_yaml_path = os.path.join(os.path.dirname(__file__).split("Base")[0], "Conf/conf.yml")
# According to the read conf.yml To obtain the testing website service and other information
conf_server_info = YamlFileOption.read_yaml(conf_yaml_path)["server_info"]

base_url = conf_server_info["protocol"] + '://' + conf_server_info["base_url"]
verify = conf_server_info["verify"]


def start_run_case(params_object, params_mark: Union[Text, int], checker=None, session_connection=None, params=None,
                   data=None, json=None, files=None, url_converter=None, **kwargs):
    logging.captureWarnings(True)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    ost_req_resp = ost_http_runner(params_object, params_mark, base_url=base_url, verify=verify, checker=checker,
                                   session_connection=session_connection, params=params,
                                   data=data, json=json, files=files, url_converter=url_converter, **kwargs)
    return ost_req_resp.response.dict()


if __name__ == "__main__":
    ...
