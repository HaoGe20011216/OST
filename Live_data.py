#!/user/bin/env python
# -*- coding: utf-8 -*-
import json
import time

from Project_Tools.File_Tools import Tools
from conftest import push_flow_ID, Meet_Room_ID


class Main_Function_Test_Suite_Data:

    CONF_IP = Tools.read_conf_yaml_file()

    @classmethod
    def BS_login_Data(cls):
        RequestData = {
         "UsrName": "admin",
         "UsrPwd": "yanfa123!"
         }
        headers = {
            "Type": 5,
            "Info": Tools.Ebase64(json.dumps(RequestData))
        }
        return headers

    @classmethod
    def Add_Devices_Area_Data(cls):
        lst = []
        for i in range(1,3):
            encryption_data = {
                    "AreaName": f"add_area_{i}", # 去重名
                    "AreaGuid": Tools.UUID(),
                    "AreaType": i # 1:用户类型  2：终端类型
                }
            live_data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ({"Data": Tools.Ebase64(json.dumps(encryption_data))})
            )
            lst.append(live_data)
        return lst

    @classmethod
    def Add_Devices_Data(cls):
        lst = []
        for i in range(1, 11):
            Device_Name = f"www_app_{i}"  # 设备名称
            Device_AreaGuid = ""  # 设备分区GUID
            Device_Type = 1  # 1是安卓， 3是PC
            if i > 5:
                Device_Name = f"www_pc_{i}"  # 设备名称
                Device_Type = 3  # 1是安卓， 3是PC

            RequestData = {
                "DeviceName": Device_Name,  # 设备账户名
                "DeviceNickName": Device_Name,  # 设备昵称
                "DeviceGuid": Tools.UUID(),  # 设备GUID
                "DevicePwd": Device_Name,  # 设备密码
                "DeviceToken": "mo",  # 设备Token
                "DeviceAreaId": Device_AreaGuid,  # 设备所在分区GUID
                "DeviceIp": "192.168.4.183",  # 设备IP
                "DevicePriority": 2,  # 设备级别
                "DeviceStatus": 1,  # 设备状态
                # 1：空闲，2：在线，3：喊话中，4：对讲中，5：呼叫中，6：被呼叫中，7：广播中，8：监控中，9：会议中，10：会议呼叫中
                "HasVid": 1,  # 有无视频 1有 2无  integer
                "HasTalk": 1,  # 有无对讲 1有 2无 integer
                "RtspUrl": "",  # rtsp地址
                "DeviceType": Device_Type,  # 设备类型  integer
                "PlayTalkVol": 60,  # 对讲的播放音量 integer
                "PlayBcVol": 60,  # 广播的播放音量 integer
                "PlayBellVol": 60,  # 铃声的播放音量 integer
                "CallTalkVol": 60,  # 采集的对讲音量 integer
                "CallWatchVol": 60,  # 采集的监视音量 integer
                "TimeStamp": Tools.Time(),  # 时间戳
                "CustomBtns": []
            }  # 加密数据体
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ({"Data": Tools.Ebase64(json.dumps(RequestData))})
            )
            lst.append(data)

        return lst

    @classmethod
    def Add_Timed_Task_Data(cls):
        data_lst = []
        device_Guid_list = []
        device_Name_list = []
        sql = "  select Fld_User_Guid, Fld_User_NickName FROM Tbl_TerminalInfo WHERE Fld_User_NickName LIKE 'www_app_%'  "
        for device in Tools.mysql(cls.CONF_IP, sql).fetchall():
            device_Guid_list.append(device[0])
            device_Name_list.append(device[1])
        if device_Guid_list == []:
            sql = "select Fld_User_Guid, Fld_User_NickName FROM Tbl_TerminalInfo limit 3"
            for device in Tools.mysql(cls.CONF_IP, sql).fetchall():
                device_Guid_list.append(device[0])
                device_Name_list.append(device[1])

        counter = 0
        for loop in device_Guid_list:
            Task_Guid = Tools.UUID()
            s = push_flow_ID()
            encryption_data = {
                "BcSrcType": 2,  # 1 integer   广f播任务源类型 1: 空源, 2: mp3文件, 3: txt文件, 4: 指定声卡

                "DstDeviceGuid": [f"{loop}"],  # 2  array  目标播放列表GUID   设备播放列表

                "DurationType": 2,  # 3  integer  持续时长类型 1: 文件计算 2: 手动选择

                "PlayMode": 1,  # 4 integer  播放模式 1: 顺序播放 2: 随机播放 3: 单曲循环 4: 列表播放 5: 单曲播放

                "SrcFileLists": [s[1]],  # 5  array  文件播放列表GUID

                "TransProto": 1,  # 6 integer 数据传输方式 协议类型 1:TCP 2: UDP 3: UDP组播 4: RTP 5: RTP组播 6: RTSP 7: RTMP

                "TskDuration": 300,  # 7  integer  任务持续时长

                "TskFileSec": 0,  # 8 integer 音源文件时长

                "TskFree": 2,  # 9  integer  是否冻结任务

                "TskJobType": 1,  # 10 integer 任务的工作类型 1 每天 2 临时 3 每周

                "TskName": f"Task_{device_Name_list[counter]}",  # 11 string 任务名称

                "TskPlayVolumn": 35,  # 12 integer 播放音量

                "TskPrePowerSec": 0,  # 13 integer 预开功放时长

                "TskPrio": 16,  # 14 integer 任务优先级

                "TskGuid": Task_Guid,  # string 任务guid

                "TskProjGuid": "XXXX",  # 15 string 任务所属方案guid

                "TskRestore": 1,  # 16 integer 任务被切换后是否恢复  1 恢复 2不恢复

                "TskStartTime": str(Tools.Time()),  # "1706292629",#, # 17  string 该任务的开始时间(定时)

                "TskPlayStartTime": str(Tools.Time()),  # 该任务的开始运行时间(手动)

                "TskStopTime": "",  # 18 string 任务结束时间

                "TskTmpFreezeDate": [],  # 19 array items: integer 冻结期限日期

                "TskWeekData": "0000000",  # 20 string 每周任务哪几天执行 0110011 即表示周二，周三，周六，周日需要播放

                "TskStatus": 1,
                # 任务状态 1：空闲，2：自动运行，3：手动运行，4：开始呼叫，5：呼叫接通，6：呼叫无响应，7：任务启动失败，8：任务过期 9：未知错误 10：呼叫取消 11：呼叫转移 12：呼叫拒绝

                "TskStreamID": s[0],  # 推流ID

                "MdTp": 2,  # integer 数据类型 1视频, 2音频, 3音视频

                "TskAuto": 2,  # 任务自动还是手动执行 1手动 2自动   int

                "TskStreamUrl": f"rtmp://{cls.CONF_IP}:1937/BS/{Task_Guid}"  # 任务的流地址 RTMP/RTSP
            }
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ({"Data": Tools.Ebase64(json.dumps(encryption_data))})
            )
            counter += 1
            data_lst.append(data)
        return data_lst

    @classmethod
    def Add_Video_Meet_Data(cls):
        meet_guid = Tools.UUID()
        Video_Mumber_list = []
        sql = "  select Fld_User_Guid, Fld_User_NickName FROM Tbl_TerminalInfo WHERE Fld_User_NickName LIKE 'www_app_%' limit 60 "
        Device_Guid = Tools.mysql(cls.CONF_IP, sql)
        for video_number in Device_Guid.fetchall():
            Video_Mumber_list.append({"UsrId": video_number[0], "MeetGuid": meet_guid, "MeetState": 4})

        encryption_data = {
            "MeetName": f"MeetHost_{Tools.Time()}",  # string    会议房间名称

            "MeetGuid": meet_guid,  # string    会议任务GUID

            "MeetNum": Meet_Room_ID(),  # integer   会议房间号

            "MeetBeginTime": Tools.Time(),  # integer   会议开始时间

            "MeetEndTime": 0,  # integer   会议结束时间

            "MeetMaxPeople": 64,  # integer    会议最大人数 最多64

            "MeetLayoutType": 1,  # integer   会议布局类型 1:自动 2:3*3 n:(n+1)*(n+1) n:max=8

            "MeetVol": 85,  # integer    会议音量

            "MeetRation": 3,  # integer   会议分辨率类型 1:640 2:720 3:1080

            "MeetPwd": "",  # string  会议密码

            "MeetState": 1,  # integer    会议状态 1:未开始 2:进行中 3:结束 4:开始

            "MeetCompereGuid": Video_Mumber_list[0]["UsrId"],  # string    会议主持人

            "MeetUrl": f"https://120.76.133.241:30443/?MeetGuid={meet_guid}",  # string  会议URL

            "Meeters": Video_Mumber_list,  #  array 与会者GUID， 会议任务guid， 与会者状态
            # 与会状态 1 申请中 ，2 拒绝 ，3 通过 ，4 在线 ，5 离线

            "MeetType": 2  # integer   会议模式 1主席 2自由
        }
        data = (
            ('["Verify"]', {"TimeStamp": Tools.Time()}),
            ({"Data": Tools.Ebase64(json.dumps(encryption_data))})
        )
        print(data)
        return data

    @classmethod
    def Delete_Devices_Data(cls):
        lst = []
        sql =  "   select Fld_User_Guid FROM Tbl_TerminalInfo WHERE Fld_User_Name LIKE 'www%'  "
        Device_Guid = Tools.mysql(cls.CONF_IP, sql)
        for guid in Device_Guid.fetchall():
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ('["Param"][0]', {"Value": guid[0]})
            )
            lst.append(data)
        return lst

    @classmethod
    def Delete_Area_Data(cls):
        lst = []
        sql = " select Fld_AreaID from Tbl_Area where Fld_Name like 'add_area_%'  "
        Area_Guid = Tools.mysql(cls.CONF_IP, sql)
        for guid in Area_Guid .fetchall():
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ('["Param"][0]', {"Value": guid[0]})
            )
            lst.append(data)
        return lst

    @classmethod
    def Delete_Time_Task_Data(cls):
        lst = []
        sql = "  SELECT Fld_Tsk_Guid FROM Tbl_Broadcast_Task where Fld_Tsk_Name like 'Task_%'  "
        Timed_Task_Guid = Tools.mysql(cls.CONF_IP, sql)
        for time_task_guid in Timed_Task_Guid.fetchall():
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ('["Param"][0]', {"Value": time_task_guid[0]})
            )
            lst.append(data)
        return lst

    @classmethod
    def Delete_Video_Meet_Data(cls):
        lst = []
        sql = "  SELECT * FROM Tbl_MeetingRoom where Fld_MeetName LIKE 'MeetHost%'  "
        Meet_Guid = Tools.mysql(cls.CONF_IP, sql)
        for meet_guid in Meet_Guid.fetchall():
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ('["Param"][0]', {"Value": meet_guid[2]})
            )
            lst.append(data)
        return lst

    @classmethod
    def Stup_Timed_Task_Data(cls):
        lst = []
        sql = "  SELECT Fld_Tsk_Guid FROM Tbl_Broadcast_Task where Fld_Tsk_Name like 'Task_%'  "
        Timed_Task_Guid = Tools.mysql(cls.CONF_IP, sql)
        for time_task_guid in Timed_Task_Guid.fetchall():
            data = (
                ('["Verify"]', {"TimeStamp": Tools.Time()}),
                ('["Param"][0]', {"Value": time_task_guid[0]})
            )
            lst.append(data)
        return lst


if __name__ == "__main__":
    ip = "192.168.5.181"
    sql = "  SELECT * FROM Tbl_MeetingRoom where Fld_MeetName LIKE 'MeetHost%'  "
    Timed_Task_Guid = Tools.mysql(ip, sql)
    for i in Timed_Task_Guid.fetchall():
        print(i)