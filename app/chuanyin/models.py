'''
Author: kevincnzhengyang kevin.cn.zhengyang@gmail.com
Date: 2025-08-25 23:27:15
LastEditors: kevincnzhengyang kevin.cn.zhengyang@gmail.com
LastEditTime: 2025-08-25 23:27:19
FilePath: /mss_chuanyin/app/chuanyin/models.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''

from pydantic import BaseModel


class Subscriber(BaseModel):
    platform: str   # "telegram" or "line"
    user_id: str

class Message(BaseModel):
    name: str
    symbol: str
    tag: str
    ohlc: dict
