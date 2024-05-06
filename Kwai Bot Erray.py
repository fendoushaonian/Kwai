import time
import Kwai
from Kwai import *

"""
Kwai 开发者 : 刘鸿运
      年龄  :  18
      提示  : 不会用的,别说Kwai垃圾,不要给自己技术找借口!
      介绍  : 由刘鸿运使用Kwai库,制作的快手简单评论区机器人
      示例,可以外对接ChatGPT解答问题,请勿使用Kwai库做违反
      国家法律的事情,开发者只是一个为爱追寻的人,谢谢大家支持.
"""

# 导入我的Cookie
Kwai.Cookie = "kpf=PC_WEB; clientid=3; did=web_7c509af287330621bd609912396bed1a; didv=1709202806357; soft_did=1619580708547; _bl_uid=61lL2vOnqb2q2zo29dv9mXF0mkkm; apdid=a139f7f9-bcd6-47f4-aa41-874e761f8dd2d4d4718927702caa5f95b6ad527b19c5:1714889322:1; kuaishou.web.cp.api_st=ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqAB713vvThjYLfPQotxtD0QbarnE1ok81o6eYgjWoj_E9O9enR_zV_RhATrpfQAwy34Yxk6gM3xIDJuVn0cpRTniEtgBwC6Xhz1qFlXhB9ZRZsuppLQTGwrOZ4YENlgmXON6YUmEjKHu5YUAjAdj0BpeJELl0mB3Go1ufDdmbrdYnB87UYFg8ko73zLZkS3eibC3XN0eOvfK7OPhUWaRLWPjRoS5chRQW6SqZPkVQK0_1mRhJ1XIiDALWtJLZsMPCJA9gcLMI-WITmfqZwnpIB91SuD3hM3YCgFMAE; kuaishou.web.cp.api_ph=16c3425cf50eea321ffcf46ecee40e52cac5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f1f89d049a61-0ef74a8475b5f98-26001d51-921600-18f1f89d04ae85%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22app_share%22%2C%22%24latest_utm_medium%22%3A%22app_share%22%2C%22%24latest_utm_campaign%22%3A%22app_share%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmMWY4OWQwNDlhNjEtMGVmNzRhODQ3NWI1Zjk4LTI2MDAxZDUxLTkyMTYwMC0xOGYxZjg5ZDA0YWU4NSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f1f89d049a61-0ef74a8475b5f98-26001d51-921600-18f1f89d04ae85%22%7D; ak_bmsc=789ED8AA3E76357F60D4860164970E58~000000000000000000000000000000~YAAQFdgjF0kqMzOPAQAA0b0JTBe5qnTJpFnoppCHG4vQ23nXjutySk2GDLloXKxM9DulmWr1hyT3vdMWqBxmpIFNrGYD5BWZuhs4/3NpQ9F6R+Yz4oPqcsrDd0CkMZDcD+775u8mmWu55iBb+mIHsnatStHgLfX7JvndaD7ap4eWdkUng8yJAYjGI67Ja5z7GrO0YbRfz8xuNfDkry7FVdoXeYkiiuXNCvEI+v614frHxGDNHXJPSz1OxTlC+FL9PCZEEptD0JCQ3VyqLYeShq3wbLaQYZlTpyEyeJIg9sC7N2udWu/5RRKsdBvN5ACdOXpZrP9zmYo+H/yM+rb2VHwdRULq3FYnlzOOhL+U7glch6d0MjuW5+G5o8E+nJqzDo4rSU7intSuBiUa6FCOqjUPPXGJsRZA35VLkA==; userId=1449407088; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqAB_ZSshDNi9paaj0bGTCIF1QjJpnZmQXT_09DrynnCUxdpctIJ2IB8WiYdgEdMgZaqjbNfqTNc93FJumCxFctth_Lae9V9VDOOlV_IN6yyYg-ZHMZ0SxlMn4BKjE8sY2azClxKG8oH6mlpLWB298xJpgLqVoEWJC9jN2SFh8Sxlz_35gtMqdqyulou4cwb0QgsQTlPKfyY4Yg6uo7-PsgUKxoSuDcrlwmr6APhXfdZrBO5uo0FIiClBoaEQMJcx8f-4EwmDkF1Iv8skYilazs7-E84jt4_KSgFMAE; kuaishou.server.web_ph=eae143cca67824b7e1c9e84ef9320e78135a; kpn=KUAISHOU_VISION"

# 获取自己账号
Auto = Get_Auto_User()
auto_id = Auto['data']['id'] # 快手号
auto_name = Auto['data']['name'] # 快手名
# 获取账号的User_ID
auto_user_id = Account_ID(auto_id) # 快手号转快手用户ID

# 锁定评论区当机器人的链接
video = Get_Video_stream_UserID("https://www.kuaishou.com/short-video/3xc5renwhyfc2me?authorId=3x3bpwctn2r547e&streamSource=profile&area=profilexxnull")
# 获取视频ID
video_id = video['data']['video_id']
# 获取视频用户ID
user_id = video['data']['user_id']

# 无限循环
while True :

    # 获取评论区前几十条内容
    user_cotent = Get_Comments(user_id,video_id)

    # 打印输出登录信息
    print(f"当前登录账号信息:\n"
          f"快手号:{auto_id}\n"
          f"快手名:{auto_name}\n")

    # 循环快手评论区评论内容
    for content in user_cotent['message']['content'] :

        # 创建一个变量当做是否被拉黑标识符
        is_break = ''

        # 检测用户是否给我账号拉黑
        if Search_Black(content['user_id'])['user_black'] == True :
            # 账号被拉黑提示我
            is_break = "1"
        else: # 如果没有被拉黑
            is_break = "0"

        # 检测评论区内容是否有关键字 关注我 且账号没有被拉黑
        if content['content'] == "关注我" and is_break == "0" :
           if content['user_id'] == auto_user_id :
            print(f"{auto_name}不能关注自己!")
           else:
               # 关注用户
                Follow(content['user_id'])
                print(f"{auto_name}关注了{content['user_name']}\t{content['user_id']}")
        elif content['content'] == "关注我" and is_break == "1":
            print(f"{auto_name}被{content['user_name']}\t{content['user_id']}拉黑了!")
        else:
            print(f"{content['user_name']}\t{content['content']}")

    time.sleep(3) # 每3秒检测一次