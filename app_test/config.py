#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/7/19 20:29


import os
# # 项目的路径
# ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# # log 的路径
# LOG_PATH = os.path.join(ROOT_PATH, 'log')
# if not os.path.exists(LOG_PATH):
#     os.mkdir(LOG_PATH)
#     # os.makedirs()
# # 截图位置
# IMG_PATH = os.path.join(LOG_PATH, 'img')
# if not os.path.exists(LOG_PATH):
#     os.mkdir(IMG_PATH)

# 项目的路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_IMG = os.path.join(BASE_PATH, 'log_img')

LOG_DIR = os.path.join(BASE_PATH, 'logs')

CONF_DIR = os.path.join(BASE_PATH, 'confs')
CONF_FILE_PATH = os.path.join(CONF_DIR, 'cases.conf')
CONF_USER_FILE_PATH = os.path.join(CONF_DIR, 'users.conf')

if os.path.exists(LOG_IMG):
    pass
else:
    os.mkdir(LOG_IMG)

