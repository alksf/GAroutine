#!python3.6
#coding: utf8

import sys

###############
# GLOBAL VARS
###############

SipServer = '192.168.5.254'
NtpServer = '10.161.42.1'
# 192.168.0.253 - ntp для Катодов и РусАТ-а
Org = 'rusat'

###############
# USERS
###############

UsersSrc = [
# 20200220
    ['7227', 'Миева Алин Иговна', 'p@pi7duYY'],
    ['7192', 'Оикова Татяна Влаировна', 'zpEdi!ZLSAX'],
    ['7161', 'Ницкий Михаил Яноич', '*vXl#!xH@G'],
    ['7162', 'Щаков Григрий Леоович', 'UA$@lAHox'],
    ['7163', 'Кткин Игор Алексавич', 'Qt1kAFq%'],
    ['6243', 'Грьев Евгей Алексович', '^gXkg8%xf'],
    
    ]

###############
# FUNCTIONS
###############

def ShortName(full_name):
    res = ''
    res = full_name.split()[0] + " " + full_name.split()[1][0] + "." + full_name.split()[2][0] + "."

    return res

def GenConfig(users):
    res = ''
    file_name = users[0] + '.cfg'
    auth_name = Org + '-phone-' + users[0] + '@tvel.ru'
    user_name = users[0]
    password = users[2]
    display_name = users[0] + " " + users[1] #ShortName(users[1])
    label = display_name
    res = """#!version:1.0.0.1

### This file is the exported MAC-all.cfg.

account.1.auth_name = """ + auth_name + """
account.1.codec.pcma.priority = 1
account.1.codec.g729.enable = 0
account.1.codec.g729.priority = 0
account.1.codec.g722.enable = 0
account.1.codec.g722.priority = 0
account.1.display_name = """ + display_name + """
account.1.enable = 1
account.1.label = """ + label + """
account.1.sip_server.1.address = """ + SipServer + """
account.1.user_name = """ + user_name + """
account.1.password = """ + password + """
local_time.dhcp_time = 1
local_time.ntp_server1 = """ + NtpServer + """
local_time.summer_time = 0
"""

    final_file = open(file_name, 'w', encoding='utf-8')
    final_file.write(res)
    final_file.close()
    print('Config file: ', file_name, ' сформирован.')



for i in UsersSrc:
    GenConfig(i)
