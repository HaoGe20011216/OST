#!/user/bin/env python
# -*- coding: utf-8 -*-
import logging
import allure
from Base.requestEngine import start_run_case
from Live_data import Main_Function_Test_Suite_Data as data_class
from Parameter.yamlChoice import Main_Function_Test_Suite

@allure.feature("主要功能接口套件")
class Test_Main_Function_Test_Suite:

    @allure.severity("blocker")
    @allure.story("Test test_BS_Login")
    @allure.title("测试web端的登录")
    def test_BS_Login(self):
        EQ = (("body.Code", 1), ("body.Type", 5))
        result = start_run_case(Main_Function_Test_Suite, "登录", EQ, json=data_class.BS_login_Data())
        logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Add_Device_Area")
    @allure.title("测试新增设备分区")
    def test_Add_Device_Area(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiQTEwMDIifQ==")
        for data in data_class.Add_Devices_Area_Data():
            result = start_run_case(Main_Function_Test_Suite, "新增设备分区", EQ, json=data)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Delete_Area")
    @allure.title("测试删除分区")
    def test_Delete_Area(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiRDEwMDIifQ==")
        for data in data_class.Delete_Area_Data():
            result = start_run_case(Main_Function_Test_Suite, "删除设备分区", EQ, json=data)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Add_Devices")
    @allure.title("测试新增设备， 包括安卓，PC")
    def test_Add_Devices(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiQTEwMDQifQ==")
        for data in data_class.Add_Devices_Data():
            result = start_run_case(Main_Function_Test_Suite, "新增设备", EQ, json=data)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Add_Timed_Task")
    @allure.title("新建定时任务")
    def test_Add_Timed_Task(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiQTEwMTIifQ==")
        for data in data_class.Add_Timed_Task_Data():
            result = start_run_case(Main_Function_Test_Suite, "新增定时任务", EQ, json=data)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Stop_Timed_Task")
    @allure.title("停止定时任务")
    def test_Stop_Timed_Task(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiTTEwMDYifQ==")
        for data in data_class.Stup_Timed_Task_Data():
            result = start_run_case(Main_Function_Test_Suite, "停止定时任务", EQ, json=data)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Delete_Timed_Task")
    @allure.title("删除定时任务")
    def test_Delete_Timed_Task(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiRDEwMTIifQ==")
        for data in data_class.Delete_Time_Task_Data():
            result = start_run_case(Main_Function_Test_Suite, "删除定时任务", EQ, json=data)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Add_Video_Meet")
    @allure.title("新增视频会议")
    def test_Add_Video_Meet(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiQTEwMTYifQ==")
        result = start_run_case(Main_Function_Test_Suite, "新增视频会议", EQ, json=data_class.Add_Video_Meet_Data())
        logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Delete_Video_Meet")
    @allure.title("删除视频会议")
    def test_Delete_Video_Meet(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiRDEwMTUifQ==")
        for video_meet in data_class.Delete_Video_Meet_Data():
            result = start_run_case(Main_Function_Test_Suite, "删除视频会议", EQ, json=video_meet)
            logging.info(result)

    @allure.severity("blocker")
    @allure.story("Test test_Delete_Devices")
    @allure.title("删除设备")
    def test_Delete_Devices(self):
        EQ = ("body", "eyJDb2RlIjoxLCJSZXFDb2RlIjoiRDEwMDQifQ==")
        for data in data_class.Delete_Devices_Data():
            result = start_run_case(Main_Function_Test_Suite, "删除设备", EQ, json=data)
            logging.info(result)





