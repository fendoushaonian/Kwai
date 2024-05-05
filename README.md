# Kwai 制作时间 : 2024/4/30
<b sytle="color:red">仅供学习参考,请勿违反当地国家的法律,作者不会承担任何责任.</b><br/><br/>
开发者微信号码 : q1523543428<br/>
亲爱的朋友们，让我为大家带来一个颇具传奇色彩的故事和一款实用的工具——Kwai库！<br/>
Kwai库是基于Python语言开发,Kwai库作用是能够使用快手基本功能，包括开发者自制功能.

## Kwai库背后的故事
它的创作者，是一位年仅18岁的热血少年，名叫刘鸿运。而这款Kwai库的诞生，背后还隐藏着一个温馨而又有些小插曲的故事。话说几天前，刘鸿运的快手账号被前女友程羽悄悄地拉黑了。这个善良又执着的少年，一直默默地喜欢着程羽，但快手的限制却阻挡了他追寻爱情的视线。于是，他下定决心，要打破这个屏障！

## Kwai库的功能介绍

### Kwai 1.1库更新内容 更新时间 : 2024/5/5
+ 快手发送短信
+ 快手账号登录
+ 无视快手封禁IP，风控，被封禁也可以接着继续使用Kwai 1.1采集数据
+ 提供逆向快手https://cp.kuaishou.com/profile 地方JS文件，大家自己补环境
+ 快手个人主页链接取用户ID

### 1. 快手基础功能
+ 关注与取消关注
+ 快手视频发评论
+ 快手用户举报
+ 快手推荐视频
+ 快手猜你喜欢
+ 快手开播状态
+ 快手当前账号信息
+ 推荐视频浏览
+ 账号转ID查询
+ 快手个人主页链接取用户ID
+ 快手账号登录
+ 快手发送短信

### 2. 独特黑科技
+ 检测快手账号是否被拉黑
+ 提取视频和用户ID
+ 举报不良内容
+ 直播快手链接取快手号转用户ID
+ 快手是否正在开直播
+ 调用快手AI_小快 (半开发)
+ 获取快手用户IP地址
+ 获取快手用户星座和地址信息

### 3. 即将推出的高级功能 (Kwai 2.0版本)
+ 逆向JS技术
+ 快手AI小快交互
+ 钱包余额查询
+ 自动开宝箱
+ 自动签到

目前，Kwai库已经推出了1.0测试公测版本，并得到了广大用户的好评。而在不久的将来，Kwai 2.0版本将更加强大，将为大家带来更多高级功能。相信在刘鸿运的努力下，Kwai库一定能够帮助大家解决在快手使用过程中遇到的各种难题！
最后，让我们共同为这位才华横溢的开发者刘鸿运点赞！感谢他为我们带来了这款实用的Kwai库，让我们的快手生活更加精彩纷呈！(≧▽≦)

#### 刘鸿运自制 Python Kwai 1.0 快手库

导入Kwai库
```python
import Kwai
from Kwai import *
```

首先设置Cookie
```python
import Kwai

Kwai.Cookie = "" # 填写浏览器快手登录的Cookie值
```

常用参数解释
```python
'kwai_account' # 这个是要填写你的快手号
'user_id' # 这个需要用Kwai库函数把快手账号转为User_ID
'user_href' # 这个是要提供链接内容
'e_tag' # 这个需要用Kwai库里面Get_E_Tag()获取
'content' # 要发送的内容
'phone' # 手机号码
'sms' # 验证码
```

快手账号转User_ID
```python
from Kwai import *

# 参数 : kwai_account
Account_ID("fendoushaonianshiwo") 
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
print(user_id)

运行结果 : '3x9uynma7zwjfze'
```

获取快手单个用户内容
```python
from Kwai import *

参数 : 'user_id' # 参数 : user_id 
Search_Message() # 获取用户单个内容
```
```python
import Kwai 
from Kwai import *

Kwai.Cookie = "" 
user_id = Account_ID("fendoushaonianshiwo")
print(Search_Message(user_id))

运行结果 : {'author_name': '刘鸿运', 'data': {'user_id': '3x9uynma7zwjfze', 'user_name': '奋斗少年', 'headerurl': 'https://p4-pro.a.yximgs.com/uhead/AB/2022/02/25/21/BMjAyMjAyMjUyMTQwMjhfMTQ0OTQwNzA4OF8yX2hkNzI0XzE4Nw==_s.jpg'}}  
```

检测快手账号是否被拉黑
```python
from Kwai import *

# 参数 : user_id
Search_Black()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
print(Search_Black(user_id))

运行结果 : {'author_name': '刘鸿运', 'user_black': False}
```
快手可能感兴趣的人
```python
from Kwai import *

# 无需任何参数
Search_Interested()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
print(Search_Interested())

运行结果 : {'author_name': '刘鸿运', 'Number': '6', 'User': [{'Name': '攀登歌', 'ID': '3xfwqvbt9uza7km', 'Text': '用歌声演唱人生百态', 'Link': '通讯录好友', 'Header': 'https://p4-pro.a.yximgs.com/uhead/AB/2020/02/24/15/BMjAyMDAyMjQxNTMzMDJfMTc5ODQzNzQ0Nl8xX2hkMjAxXzk3Mg==_s.jpg'}, {'Name': '小许不是指南（期末挂科）', 'ID': '3x7pxqg3g6audcs', 'Text': '用户太懒了,没有设置简介', 'Link': '你可能认识的人', 'Header': 'https://p2-pro.a.yximgs.com/uhead/AB/2021/07/28/19/BMjAyMTA3MjgxOTE0MzBfODc2MzIxMjk4XzJfaGQ1NjdfMjA5_s.jpg'}, {'Name': '我的小熊想见你', 'ID': '3xmuhuigijiu4fy', 'Text': '本人很差', 'Link': '你可能认识的人', 'Header': 'https://p2-pro.a.yximgs.com/uhead/AB/2021/05/31/15/BMjAyMTA1MzExNTU1NTVfMTkyMjE4MTEyM18yX2hkNTc4XzI5NA==_s.jpg'}, {'Name': '达咩.✘', 'ID': '3x3fwt9ytame4hk', 'Text': '总要学会长大叭...', 'Link': '你可能认识的人', 'Header': 'https://p5-pro.a.yximgs.com/uhead/AB/2024/01/19/22/BMjAyNDAxMTkyMjUzNTVfMjE5NDEyNjk4XzJfaGQzXzUxNA==_s.jpg'}, {'Name': '晨ㅤ', 'ID': '3xjd3mciax9rgj9', 'Text': '你 我梦中常客', 'Link': '你可能认识的人', 'Header': 'https://p2-pro.a.yximgs.com/uhead/AB/2024/04/18/11/BMjAyNDA0MTgxMTEyMTJfMTg2MDI4NjQ2N18yX2hkOTExXzUwMw==_s.jpg'}, {'Name': '奋斗少年', 'ID': '3x9pqvkb95wxfq4', 'Text': 'QQ查Q绑官方群:未\n本人16岁，非诚勿扰！谢谢\n，快手标黑客的直接退出就行，\n都是假的，真黑客不会名字叫黑客，\n再说黑客也是人，也怕条子，那些作品\n都是百度他们搜的，试过的小伙伴知道基本\n没啥效果', 'Link': '通讯录好友', 'Header': 'https://p2-pro.a.yximgs.com/uhead/AB/2021/04/08/00/BMjAyMTA0MDgwMDQzNDJfMjIwOTI4Mjg4MV8yX2hkNzk3XzY4Ng==_s.jpg'}]}
```
快手推荐视频
```python
from Kwai import *

# 无需任何参数
Recommendation()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
print(Recommendation())

运行结果 : {'author_name': '刘鸿运', 'Content': [{'title': '原来以为相遇不易后来发现重逢更难 #热 #别怕我伤心 @快手热点(O3xddgkd5fav5if9) @会火(O3xen9civbrbibgk)', 'linkCount': '8.4万', 'viewCount': '528986', 'realLikeCount': 84365, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/n-6v-Xu9_DIqgN_Pw5Dd3b4qEQVZEKYg79EsFlp_toej8kpzDbPGvzluMILlU4ax1Jg5A_xNcTUhz3IocO2v-8KIfuCoaN2p0oF_IlfZj5uwAlmbVG_zlR3n9lcV93QC.mp4?pkey=AAULl1NaiMGmC2gSH3wQH822dAkbUQnemw3XGXrDDmY_MbDWmxRWp1zo3cOgigTbc1INfByNlNZdQKpo5Y54QTrL3fHlIbNZWhoX9Kcx74abE0ci5TyoRmQt5ujGwoU7J-M&tag=1-1714567643-unknown-0-h31y9qo5k9-56fe215507b29441&clientCacheKey=3xyzfgxqtw97i6c_b36106aa&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '……', 'linkCount': '2.6万', 'viewCount': '415807', 'realLikeCount': 25717, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/DOJ6kuU7i3ddtLOK73B0o4083lfyE_G38r4LYp3UsHXpZPKz1wt1m69mPzzPIRjhX6raKWMN7wDZbx9n-6j6GLEEMSy0c4c-yIyhS8IMxbBxeV1EuIcuDxFC_q-Vksq7.mp4?pkey=AAXSKn0TrKW2QEcYPtE-0ckIONbxSh7verOrHsH8qvF8D62srBpA2AzwEHs1OfAyG6edxvnehg2qGLHmXLfOFD-32ZMhQPXxoHXuqHexrFnRFG3AWr0btagGOSbh_SObUqc&tag=1-1714567643-unknown-0-g5rbva5tpt-c2adc28e41abc3c8&clientCacheKey=3xjk8yhjq7n76b6_38d342bf&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '#提到了你 @会火(O3xen9civbrbibgk)', 'linkCount': '5.7万', 'viewCount': '1694403', 'realLikeCount': 57022, 'photoUrl': 'https://v1.kwaicdn.com/ksc2/qjhBJh4f1zp9zgEaQ6BRmt3qYp5hZ6F3dJIyeLf_SAfzugcPrXeV0T9mvVWjbl9XLLjnb8cjzEMgPTocwRQcYOE4RYM9JEmfQvHwap7riHNdivnSypzDiZw-COaNV2Bg.mp4?pkey=AAVhH73xoKaoDFAxx6alDxgeYLEdkP9u25qYyspnYBsNk8gnTosRcDt2xjCsKHOfLK_83ZyIx13iT3BRV9VRssaLNnKou8auyOyfSXCX7P0LAt2E1b1uHXQWTX8VWvuX16k&tag=1-1714567643-unknown-0-80uedi6xvi-b5b14c30d9335dc6&clientCacheKey=3x6c52wfm9h85ek_4a3ed72a&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': ' @沅妹（阿宇不一般）(O3xzni35yqii642g) 的精彩视频', 'linkCount': '1.8万', 'viewCount': '583472', 'realLikeCount': 18063, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/V_YdUGhOjtlewL3P3vjjmQxdlh4jmHUc8Mn4B108AoNMlgVp3RI6zkXwKiAihgNZbaqRrkISRQjtgg_LnueYkIyuLSGgSpvFNR87mqi75Qf143Y1kJQaD1Zq4_kn-Fqs.mp4?pkey=AAUpP3q26eZXYXqr8hVau945ibIAQegPIi7hJemt6FtYxJU0gSik8Ip-_4grGSNAogut1zd6up18K12L1D2fJ_tjr7uPE9kRqXkjWNRn4YrjxFBOCMuctZtq0xTgFlFkhB8&tag=1-1714567643-unknown-0-66zsdcnfqb-787b2d6778efeb20&clientCacheKey=3xjcu4gnnud4h4m_d2ed3963&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '这个棒棒糖🍭也太浪漫了吧~你的宝子给你安排了吗?#520礼物 #仪式感不能少 #惊喜 @快手热点(O3xddgkd5fav5if9) @热门小助手(O3xknkmgwkexnr54) @快手创作者中心(O3xrgtux2ehryffe)', 'linkCount': '2397', 'viewCount': '168626', 'realLikeCount': 2397, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/u8GdOM0H3RPhCbsdbjlToi04mzjNmgkrW6Hb6UTxTkBeK8Dt7Ew4_mPRFZqfBuib9nV8oN23F5M7MsbNqoyIbDsbA_qw7OSZ9juBWXxoi1oeEePOdKKWv86MAPeyMgc_.mp4?pkey=AAW4yaTWgBTr95YFVgKE_SgCKZxmsppzB_ZiPWNwKzGTo6OPZqv5Zjoynfwo6D6l-7-yP7__Odjphh063eS6tveXISJ6KWYIwpjx3AgnxF6q1U-es22CMhn_Jp7J8wKO1Rs&tag=1-1714567643-unknown-0-y0tjjc7joa-fcaa7bf7db5c0215&clientCacheKey=3x4depmdwexh7x9_dcf42118&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '惩戒营800人，硬刚德军装甲部队，800人眼里只有冲锋没有后退！', 'linkCount': '7303', 'viewCount': '335545', 'realLikeCount': 7303, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/uYZDVQqLKMcoW10P1hSjz6VpGCktFkNPhZw4n4UJDyX4drSec7Ssy_XdK2zfbQk8cktjkXLCB1qu_jD_6630ZK8zxugveP8RV6Ia7BJiimpMz8XtMrCkMsn3XZuqNCkX.mp4?pkey=AAXbANrRxN0g6LVpAVs-XT6kIQufNFuR9rh2O9C6qgqEB8v5UAw0Ym4XYgm6EWFeVhewwBfPjFwgybBOQM07WVV1NaIOzMOljfFGipjIW_VJonl1prFl7a_x_N1pXVx6PPI&tag=1-1714567643-unknown-0-7xfvo4fo6b-92de3248e419ca50&clientCacheKey=3x4gjdaab49aam6_92aed43a&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '兄弟喝过的水 你敢喝吗？ #伪人 #猎奇 #第五人格', 'linkCount': '1.2万', 'viewCount': '1042916', 'realLikeCount': 11821, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/xW-3csiuv1JyDk5Iwuc5sQBY4PO312iXcsrPL8H8Tgo1VX8_jZgKhEtfRETjeNPtjPJJSpHM64aGtsI5hOjfGudVnhyAyARhfUozhB0U2YdZB7Cb-TO5JstK5ml07uvR.mp4?pkey=AAX_MltIHHprWUGlJDYMrNxznY6PwJ53PNiwv4dfNagny-F8T4qTobDMx_Y12LOGjxxUe5RZrQDZI39CB6mcSJ_fdqEj-6z-dy4DjLlRg1cg7Fr_C9takz9l7Quhe9QrcEg&tag=1-1714567643-unknown-0-cxsh5a0qnc-5c293801bb3d02c5&clientCacheKey=3xp2gqxc4chjygw_2dc6b1af&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '美白防晒隔离三合一SPF50A++++女人必备神器，不搓泥不假白，防水防汗，敏感肌孕妇哺乳期备孕期都是可以用的，姐妹们，下方小黄车赶紧入手吧🥰🥰', 'linkCount': '2470', 'viewCount': '374134', 'realLikeCount': 2470, 'photoUrl': 'https://v1.kwaicdn.com/ksc2/pvdYi2OGRnQPsRzMP76E1yylA4IW5eJe1Zc-Oe0GXiwt0s7jOg8um3W4W5y8J8mmz87c-r6BxH8Dj6iypEdskE-0YN7cEk31iSdmhOh_SWs8ZZAs4M313VkfkKM3Nj_2.mp4?pkey=AAUISfUcHDKBxTzSRby3CF-jIkhKo6iSA2hvROKcdQpF_lHjjC_06HsZTKDRI9444aNEQ6c6dE6VbiqfLB3jErOKXLoTSrjVtCk0mQ-DIlKYKAS78wS5w0tRAQeFlBa5FvI&tag=1-1714567643-unknown-0-wv64hn75xc-d111b3ec373f6f07&clientCacheKey=3xu3awamr6xjudk_cd3f65f7&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '#王者荣耀高光时刻 #王者荣耀搞笑视频  #王者荣耀热门', 'linkCount': '1.3万', 'viewCount': '1884548', 'realLikeCount': 13411, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/qpOWTncjnKRVDB7hpis-W3HRv2__W5-zQe0BTyBhEDRxSWJwEIZSUUsj4zkgmNs_iYXjLyTcw6AvnTm75CZ31Dl_nU_yUQRqDzAgl6MrrugDF79VymkYC0vJvoZRyVh0.mp4?pkey=AAVtm6kQvC5oPlWtDyMuhNdiQrnNGX5mj7kINKrFnEPnl60CNPUvdHkmHg04jDIejR8BhLzaqhcdgiP8SeodyABETIAV0JviXaUXwgGCqNFDHzk8OXmiCbonS_FjKU_k3zM&tag=1-1714567643-unknown-0-magdxp3kmb-0e262f0da3e6da9f&clientCacheKey=3x6buetjup3k5fm_808591a8&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '【6.9发十包】泡泡植物染小绿袋【名流专属d】数量不多的清一清仓库 宝宝们抓紧时间抢购吧！ 左下角小黄车可以下单 快来看看！ 快来看看！ #短视频热卖  快来看看！大上新！！！清仓库，超低价直播间浮力！！新款放送！宝宝们快来看！！！！爆款低价好货！！实惠福利！ #短视频带货@快手卖货助手 #发现  #清仓', 'linkCount': '889', 'viewCount': '360822', 'realLikeCount': 889, 'photoUrl': 'https://v1.kwaicdn.com/ksc2/45unJN4KFPfireEmomHq6coXWHaWFiX1iRCZDUeuWTkTzAYwQc5-gC2Ra0D7vaKOzn3ZhoK3_tIEEjJvXqfDjPkexH5Ez7mgK8CpSdOQ_QtjRFMnomCoBWXnOyyjsNeppAUeWYZdYqP_ru7DZscbojhmuFO8ZnB7DnadCog-AwXObp8hqQosRpw9AOI82YfK.mp4?pkey=AAUwkJvvyqnFmrIi8AhiYzbHkwYvBGyiS6RH2O_6jcavmazEBrCzmd9K4plZ1B9i-0raj3O9Io1z0jy145Mvuc0RW4SLGnYO5mrBDDIjnAEBnY8AclkL3kEqEXn8j8O4he0&tag=1-1714567643-unknown-0-leyqfzftgo-3b038a5479f97211&clientCacheKey=3xy29hsk7tdmimq_hd15.mp4&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '“会长，当我跳完这支舞我可能已经嘎了” #惊封 #木柯 #ooc警告', 'linkCount': '14.7万', 'viewCount': '661190', 'realLikeCount': 147069, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/D-pAoDnaB6j_hCsamorTm7ans4WYH8T_nMl8oPxKsCdoN73Us4AIm4z7Y2qshfLq3C6Kn9K5U68BPQj0lh06WGheScon2zoPagDyaJXvAW97HRAo-xwlT-XETxm4A2oi.mp4?pkey=AAXayo9Glja91-dUBY1WFxL7IhIkjxe6HTuaV2KhDIa6wN9Gcitpxn8keyXpyi-KGEfqyZmFzMWfPxKeVfR4eoXX0yVOM7RPruaCJ40Z2UszhTW8wcKlNXXLdbjJOJX1SIM&tag=1-1714567643-unknown-0-8ridmv2ups-09acaf0aa1765230&clientCacheKey=3xdt38k3r2x9cqu_b90dd2d5&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '我和哥哥在大山里种植晾晒的#龙牙百合干 姐姐阿姨们吃过没有，平常用来#煲汤熬粥 都很好吃，喜欢的姐姐们都可以尝一下#百合干', 'linkCount': '1.9万', 'viewCount': '100045', 'realLikeCount': 18984, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/_lZvNkV7GkfYqQsQC9wbovyI-iflYuZYIAAsdrHWlfyM7DGQUwhImRGilN5MbswK5Gkm61q3luWwFWNkBjzjO_B3zD3nVqL1TufdqNN6IdqnP4rXS4foW1l1BxoCJRfl.mp4?pkey=AAXxt6XUUIThDwCRmDLu_0F-UeTbUDwarBV25SBdzmR3lCu7KrlAfid6db7hKiM9DlrezB2WUgUft1cMqZ-BZg9W-UEKge2YcmVzdzxMvny3zhpmFAfci-9KgXLrpzhVCuk&tag=1-1714567643-unknown-0-o2pgrzibv4-6340cbed774bdbc3&clientCacheKey=3xnadvkczan98t4_01c237a7&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': 'ROSÉ x RIMOWA小公主#朴彩英rosé', 'linkCount': '4.2万', 'viewCount': '240075', 'realLikeCount': 42207, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/lk7gmImF3VsaIyZq0cctujZOqjNfpBX6xEr8ZVfBPXpRrYfulUWW4Uzp7ncP8JOf1LlKIvPf9NX6kUVN7IiIJhVtM7_saK2rkOs9pZn7jcXVlN07PYUDNqypM7Zq8mL7.mp4?pkey=AAUvPO79aDF75qodNfoZ032Uh9IIEtMFdeinBq4WPmDAaYec2MBG3A3nqelHSivSAXY36WLGTZG4zCI2GIEvr8cRjmZzPg_NnKYyboF_f83LpHjoZgUxAaiOgpozPqws9wQ&tag=1-1714567643-unknown-0-ipbs1wxj7u-d4ae05dbcb810bfc&clientCacheKey=3xj4mi3whhaq8nu_35489fd9&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '看着还一脸委屈呢🥹#它真的好像个小宝宝 #呆萌呆萌 #萌宠日常记录', 'linkCount': '4万', 'viewCount': '297646', 'realLikeCount': 40279, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/0K8V04Irhm1RKcuy7QrDVvQu0s08pJDSqHQo0WyVYXB3WySHhyUKtuJ7UZzgZXjhtnsbzEPKh3zsZBh_rhTTFBoJmh4IkOGGkNJL6ni3KABYK8VG7MmM3n745VLgig_1.mp4?pkey=AAVDfD-JpW5I2ozz_eilBsnHHvW6qF2RT9eqNgJMZyYSGnTtWoJLvA0gZT8wLy6S-5wvoqfY8YaIdptcy6oR__g2h86H4CfpKNu7U8LfOGDgz1isfh8pRAg6HM_fEHHJoAY&tag=1-1714567643-unknown-0-btatzdqsnu-255d44f1777de080&clientCacheKey=3x52idztfmun4ia_7f9ffd17&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '有一种意难平叫相见恨晚，以后再没机会看看实力了，再见弟媳#切尔西 #蒂亚戈席尔瓦 #以球之名', 'linkCount': '7562', 'viewCount': '69889', 'realLikeCount': 7562, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/-nGpoaRwfCb3JWbqzinYzsqOfUiOm5EDoh_njTJNkJPtk1mTtqDxugmszo-GuZ2w7J368VOwMkZbESgF0tkjkceRlGPoa7Giga07o5kNDW9LDl87_QUeT_vdIcPKLxvV.mp4?pkey=AAU37Hi8Vi7BHt6DRCqe80FOiomw4QSch8VmaAqdBM5REqBgRWUly2PMuTTrUkrN9wFb4H2qX_YYl7HttaRE49zt3F1s25ZJBQ12Efqq0MnNL8kiSMzr6T_tt4uCPGipZDI&tag=1-1714567643-unknown-0-nx3yagm1cp-52cbc6e2190b3b5d&clientCacheKey=3x65d8psnritvm9_81327117&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '#祖国万岁 这才是毛爷爷时代的，🇨🇳军人#致敬一代伟人 #教育爱国', 'linkCount': '34.1万', 'viewCount': '2940957', 'realLikeCount': 340893, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/OgWULPTmfVQRL4I4ZAu9YxmMkwN9CPdABSwC-JY1LIAg6A2T4cbmS836UHPyDdRd9tMRfyfxtAsopPb8b-qHiauMOp2ib8bRN5JmV31NQaKKDpjQzh_7t3cLOD6pjZ4Z.mp4?pkey=AAXo5miUKP7YR46232vCfGJZzzGmNhh7-Bmbn6dl4-D45I5m8AlpBc8qMLObIx4wUtuRd7l9gEfIwzaMHYY9nmiUdajizNFgLqDVbQm78wXpEDoX-qKMX0lps8Yv5wnbfRM&tag=1-1714567643-unknown-0-5tqdxjjnkr-58fa02b89a42fbc7&clientCacheKey=3x3w8rkcub6ep4a_cf8d66e9&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}, {'title': '超绝小狗线条#画画', 'linkCount': '43.8万', 'viewCount': '4156593', 'realLikeCount': 438154, 'photoUrl': 'https://v2.kwaicdn.com/ksc2/rCGejonp6MGupR0eqMQkoFyQ36qk-Fzp1AJFg19BFyrxg6c38yxgA1sTaDMzew1_tn6KptA6RG_WFtvvm59Du_R7w37U5D9mZZXkP-oydwJfDF_bEGXTtCHMWLeKKAG0.mp4?pkey=AAXuTchsyZ4hBaDgDqR55VRiJK2e--e5IWE_YqY6K2QZbLkV5j37LY2C6_37_xp0FWYl-49EMPxiKxMZQJGn_C6_sfNNDsibr_01IDvo-Sj5CGMnomCASDEMIKFXbBJM24g&tag=1-1714567643-unknown-0-mzqogmp3v5-1b702c0867c06917&clientCacheKey=3xa38pe6z5mxfpk_84508d5b&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}]}
```
快手随机推荐视频
```python
from Kwai import *

# 无需任何参数
Randomly_Recommend_Videos()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
print(Randomly_Recommend_Videos())

运行结果 : {'author_name': '刘鸿运', 'Content': {'title': '分享快手小知识。#谢天谢帝 #每日打卡领流量券 #光和计划小助手中心 @快手音乐人(O3xbc5wxvzkq7dis) @快手热点(O3xddgkd5fav5if9) @快手光合计划助手(O3xxpf2m4brbf3pe)', 'linkCount': '1.6万', 'viewCount': '61361', 'realLikeCount': '15631', 'photoUrl': 'https://v1.kwaicdn.com/ksc2/U01mUOcOCjc7g8hbzH5h2XO_VQfsApV7ouvLZNNb42sxfvr1nr3tTAUvTUN0-tl4neMCJvLdCYEndqZd5Xd1T3FoTJO4vTB2uvPbiXJ5VOanosuTrC5Kklu6T1J9oMCa.mp4?pkey=AAVzXBpE9iGRgxbkw7Y1pAFdpRN0Sth0ISX62X_JlyPLQK1E01ZYf-UaIW4TrIy_9fmRCUQB4AAZt17-lWq1msZ7CkUQKCKcfD4GAVc741C36jzyG2zNm80_I3NM8t5Udmo&tag=1-1714567790-unknown-0-f8gujbjy0p-2396462f7f9636b3&clientCacheKey=3x2ygg2ji4wvhbq_d12a6553&di=JAiCGk0ZjZDxEqwLhiqazQ==&bp=14944&tt=hd15&ss=vp'}}
```
快手推荐关注用户
```python
from Kwai import *

# 无需任何参数
Recommended_Followers()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
print(Recommended_Followers())

运行结果 : {'author_name': '刘鸿运', 'Content': [{'id:3xy4ww6cgivwevg,name:张一恒,href:https://www.kuaishou.com/profile/3xy4ww6cgivwevg'}, {'id:3xx2fks9ve9czas,name:鸡哥在中东,href:https://www.kuaishou.com/profile/3xx2fks9ve9czas'}, {'id:3xbcmxjk22x6umc,name:都市时报,href:https://www.kuaishou.com/profile/3xbcmxjk22x6umc'}, {'id:3xbn8phydbsttke,name:王者荣耀秋炎,href:https://www.kuaishou.com/profile/3xbn8phydbsttke'}, {'id:3xpuzhuyptrp4ym,name:北京石景山,href:https://www.kuaishou.com/profile/3xpuzhuyptrp4ym'}, {'id:3xaizrkaxnkw3cm,name:娇娇老嫂子,href:https://www.kuaishou.com/profile/3xaizrkaxnkw3cm'}, {'id:3xavcjz4ufgmp6q,name:沫凡剪辑,href:https://www.kuaishou.com/profile/3xavcjz4ufgmp6q'}, {'id:3xfya7xk4abqdgg,name:ず×sī鸩酒の诱,href:https://www.kuaishou.com/profile/3xfya7xk4abqdgg'}, {'id:3xzqxyif525r25w,name:宝丽迪🐠,href:https://www.kuaishou.com/profile/3xzqxyif525r25w'}, {'id:3x7e4dqcnqc927s,name:七创社,href:https://www.kuaishou.com/profile/3x7e4dqcnqc927s'}, {'id:3xavehh22dye7rs,name:花花酱就酱说,href:https://www.kuaishou.com/profile/3xavehh22dye7rs'}, {'id:3xyzehcd75ahd22,name:光遇 狗不理包子,href:https://www.kuaishou.com/profile/3xyzehcd75ahd22'}, {'id:3xcit2p4ypxuni6,name:景天William,href:https://www.kuaishou.com/profile/3xcit2p4ypxuni6'}, {'id:3xt28smzmfp94qk,name:御风.,href:https://www.kuaishou.com/profile/3xt28smzmfp94qk'}, {'id:3xtgfmyx28npvb6,name:拉罐兔,href:https://www.kuaishou.com/profile/3xtgfmyx28npvb6'}, {'id:3xnyr5mdfsep6dq,name:快乐的营销号,href:https://www.kuaishou.com/profile/3xnyr5mdfsep6dq'}, {'id:3xujuaijnaevdae,name:老兵回家 孙春龙,href:https://www.kuaishou.com/profile/3xujuaijnaevdae'}, {'id:3x57q44ddunbxw9,name:荆一啸,href:https://www.kuaishou.com/profile/3x57q44ddunbxw9'}, {'id:3x42wzq3qa9wz76,name:然后观察,href:https://www.kuaishou.com/profile/3x42wzq3qa9wz76'}]}
```
快手举报用户
```python
from Kwai import *

# 参数 : user_id , Content , *ju
Report_Account() # Content : 举报信息 *ju : 214 # 默认214即可
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("2516738894")
print(Report_Account(user_id,"恶搞快手",214))

运行结果 : {'author_name': '刘鸿运', 'data': {'user_id': '3xd9jcxrap6qfi6', 'content': '恶搞快手', 'mode': 214, 'return': 'true'}}
```
快手关注
```python
from Kwai import *

# 参数 : user_id
Follow()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
print(Follow(user_id))

运行结果 : {'author_name': '刘鸿运', 'data': {'id': '3x9uynma7zwjfze', 'name': '奋斗少年', 'following': '账号被拉黑', 'follow_status': True}}
```
快手取消关注
```python
from Kwai import *

# 参数 : user_id
Cancel_Follow()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
print(Cancel_Follow(user_id))

运行结果 : {'author_name': '刘鸿运', 'data': {'id': '3x9uynma7zwjfze', 'name': '奋斗少年', 'following': '账号被拉黑', 'close_follow': True}}
```
检测快手是否关注用户
```python
from Kwai import *

# 参数 : user_id
Judging_Attention()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
print(Judging_Attention(user_id))

运行结果 : {'author_name': '刘鸿运', 'data': {'user_name': '奋斗少年', 'user_id': '3x9uynma7zwjfze', 'user_black': '账号被拉黑', 'user_following': True}}
```
获取快手当前登录账号信息
```python
from Kwai import *

# 无参数
Judging_Attention()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
Search_Key = user_id
print(Get_Auto_User())

运行结果 : {'author_name': '刘鸿运', 'data': {'id': 'fendoushaonianshiwo', 'name': '奋斗少年', 'eid': '3x9uynma7zwjfze', 'user_id': 1449407088}}
```
获取快手视频总数量
```python
from Kwai import *

# 参数 : user_id
Get_Video_Number()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
print(Get_Video_Number(user_id))

运行结果 : {'author_name': '刘鸿运', 'data': {'video_number': '1'}}
```
快手视频链接获取视频ID和用户ID
```python
from Kwai import *

# 参数 : user_href 
Get_Video_User_ID() # user_href 视频链接
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
href = "https://www.kuaishou.com/short-video/3x6jihxerwpnism?userId=3x2c7683mjqy6i9"
value = Get_Video_User_ID(href)
print(value)

运行结果 : {'author_name': '刘鸿运', 'data': {'video_id': '3x6jihxerwpnism', 'user_id': '3x2c7683mjqy6i9'}}
```
快手跳转用户账号链接
```python
from Kwai import *

# 参数 : user_id 
Get_User_Href() 
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_id = Account_ID("fendoushaonianshiwo")
value = Get_User_Href(user_id)
print(value)

运行结果 : {'author_name': '刘鸿运', 'message': 'https://www.kuaishou.com/profile/3x9uynma7zwjfze'}
```
获取快手评论过区内容(会携带回复)
```python
from Kwai import *

# 参数 : user_id 
Get_User_Href() 
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
# 获取视频id 和 用户id
user = Get_Video_User_ID("https://www.kuaishou.com/short-video/3x6jihxerwpnism?userId=3x2c7683mjqy6i9")
# 获取评论区内容
print(Get_Comments(user['data']['user_id'], user['data']['video_id']))

运行结果 : {'author_name': '刘鸿运', 'Video_Number': 1001, 'message': {'content': [{'user_id': '3x48cncatxybew6', 'user_name': '启林律所-x', 'content': '自己还哦', 'time': '2024-03-13 17:36:10'}, {'user_id': '3xbv72qsmxsyvj9', 'user_name': '华夏保险，黄', 'content': '想好梦，也没这么快吧', 'time': '2024-03-07 10:24:37'}, {'user_id': '3xccrbzk56nb7wa', 'user_name': 'AA91999999', 'content': '咋的办嘞', 'time': '2024-03-30 14:14:52'}, {'user_id': '3xtititvxe93zie', 'user_name': '爱跑步', 'content': '天真', 'time': '2024-03-23 17:51:17'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:54:55'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:54:50'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:55:03'}, {'user_id': '3xweicw6gj7x3ba', 'user_name': '4305', 'content': '不可能', 'time': '2024-03-13 08:08:54'}, {'user_id': '3xxyphtrsp7wbbw', 'user_name': '奥克斯战争', 'content': '有那么好吗？', 'time': '2024-03-05 09:58:59'}, {'user_id': '3xhwtq5cj3ttzhc', 'user_name': '小米粥粥', 'content': '推你了，看有没有', 'time': '2024-03-16 13:30:17'}, {'user_id': '3xqbirivnsra8nk', 'user_name': '奶莓软糖', 'content': '真的', 'time': '2024-03-18 17:10:12'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:57:32'}, {'user_id': '3xugv3n36p8cg49', 'user_name': '不做大哥好多年', 'content': '你给还呀，', 'time': '2024-03-10 19:28:35'}, {'user_id': '3xpik5w9wn3d3h9', 'user_name': '善良的富婆', 'content': '你说的是真的吗！要是那样想我的债务还清了，我人都是你的！', 'time': '2024-03-12 14:40:50'}, {'user_id': '3x4buuatd3dtiz2', 'user_name': '舒心彩荷', 'content': '能给我还吗', 'time': '2024-03-10 13:49:06'}, {'user_id': '3xkv8qr9vys9mka', 'user_name': 'P破茧成蝶', 'content': '那样肯定安心上班了', 'time': '2024-03-09 14:48:48'}, {'user_id': '3x6ueyztywnpcva', 'user_name': '快手用户1695698360528', 'content': '有这好事？', 'time': '2024-03-08 13:45:50'}, {'user_id': '3xtnuxf5skew5v6', 'user_name': '冀效斌，🐒', 'content': '干个秋', 'time': '2024-03-09 13:31:06'}, {'user_id': '3x8ypbtqwcqjhrq', 'user_name': 'User_1580201438591', 'content': '给我还吗？', 'time': '2024-03-12 08:06:01'}, {'user_id': '3xnz7yn6xm5dpfu', 'user_name': '震哥', 'content': '有这个好是', 'time': '2024-03-09 09:16:05'}, {'user_id': '3xavvc7rgfsmsea', 'user_name': '打假', 'content': '房贷谁给还[捂脸]', 'time': '2024-03-31 16:45:33'}, {'user_id': '3xvhh2im7zr2iu9', 'user_name': '强胜农资合作社易军', 'content': '对', 'time': '2024-03-31 16:43:09'}, {'user_id': '3xw6eehd4pk7e86', 'user_name': '邪狼，星雨步', 'content': '可能代价更大', 'time': '2024-03-31 15:45:50'}, {'user_id': '3xarranv4m9knbm', 'user_name': '王者至高', 'content': '费用是怎么收的', 'time': '2024-03-30 20:33:32'}, {'user_id': '3xpb2je992s442g', 'user_name': '衹给你～幸福', 'content': '你先给许家印办一下吧[调皮]', 'time': '2024-03-30 17:26:12'}, {'user_id': '3x84ys4dpmq4ei9', 'user_name': '一个老兵', 'content': '可以呀', 'time': '2024-03-30 16:59:53'}, {'user_id': '3x74367q7v66tt4', 'user_name': '黄金钾', 'content': '你们是吸血鬼', 'time': '2024-03-30 15:20:56'}, {'user_id': '3xx4dzssx7ckpx6', 'user_name': 'Huang', 'content': '怎么联系你', 'time': '2024-03-30 14:07:54'}, {'user_id': '3xd3x2mxt2ugbwc', 'user_name': 'User_1447322541', 'content': '真的吗？', 'time': '2024-03-30 13:57:36'}, {'user_id': '3x2yhddmsi8s9ba', 'user_name': '☞崛起☜', 'content': '天会掉馅饼吗', 'time': '2024-03-30 13:57:20'}], 'reply_content': [{'user_id': '3xnpdje2me7q6ny', 'user_name': '王鹏-鱼期咨询', 'content': '仙人', 'time': '2024-03-10 15:54:05', 'replyToUserName': '时来《运转）'}, {'user_id': '3x48cncatxybew6', 'user_name': '启林律所-x', 'content': '自己还哦', 'time': '2024-03-13 17:36:10', 'replyToUserName': '时来《运转）'}, {'user_id': '3xfnt96z5xy4xvy', 'user_name': '沐雪72', 'content': '协商解决', 'time': '2024-03-12 14:09:56', 'replyToUserName': '秦涛037'}, {'user_id': '3xjbfnwgxjcdbca', 'user_name': '轻松游影视', 'content': '怎么办？', 'time': '2024-03-22 17:12:37', 'replyToUserName': '秦涛037'}, {'user_id': '3xccrbzk56nb7wa', 'user_name': 'AA91999999', 'content': '咋的办嘞', 'time': '2024-03-30 14:14:52', 'replyToUserName': '秦涛037'}, {'user_id': '3xc62js2dntqgze', 'user_name': '此处无声¥', 'content': '你觉得有吗？', 'time': '2024-03-09 15:05:28', 'replyToUserName': '九头凤'}, {'user_id': '3xtititvxe93zie', 'user_name': '爱跑步', 'content': '天真', 'time': '2024-03-23 17:51:17', 'replyToUserName': '九头凤'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:54:55', 'replyToUserName': '源泉1461'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:54:50', 'replyToUserName': '杨琼辉'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:55:03', 'replyToUserName': '洋洋'}, {'user_id': '3xk59p3ifecxefw', 'user_name': '磊哥。，？', 'content': '能不能介绍一下', 'time': '2024-03-16 09:00:11', 'replyToUserName': '小米粥粥'}, {'user_id': '3x5fjfb35rd9bri', 'user_name': '静檀5678🌲🌲🌲', 'content': '真有这样的吗', 'time': '2024-03-16 09:15:36', 'replyToUserName': '小米粥粥'}, {'user_id': '3xhwtq5cj3ttzhc', 'user_name': '小米粥粥', 'content': '推你了，看有没有', 'time': '2024-03-16 13:30:17', 'replyToUserName': '磊哥。，？'}, {'user_id': '3xqbirivnsra8nk', 'user_name': '奶莓软糖', 'content': '真的', 'time': '2024-03-18 17:10:12', 'replyToUserName': '💞࿐请ღ᭄᭄妹妹💞࿐'}, {'user_id': '3xcg7eij4tx4xwg', 'user_name': '点击这里申请暂停还款', 'content': '@🎀有钱儿er.(O3xxnjghv5wz2hgy)', 'time': '2024-03-27 22:57:32', 'replyToUserName': '🇨🇳航天科技东方红'}]}}
```
快手获取IP和详细地址信息
```python
from Kwai import *

# 无参数 
Get_IP_Host()
```
```python
import Kwai
from Kwai import *

print(Get_IP_Host())

运行结果 : {'author_name': '刘鸿运', 'data': {'ip': '121.27.227.232', 'city': 'xxxxxx'}} # 由于获取信息太详细不写了
```
快手用户是否开启直播
```python

from Kwai import *

# 参数 : kwai_account 
Live_Streaming_Status()
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user = "fendoushaonianshiwo"
print(Live_Streaming_Status(user))

运行结果 : {'author_name': '刘鸿运', 'start': False} # False 代表没有 True代表有
```
快手直播链接取快手号 自动转用户ID
```python

from Kwai import *

# 参数 : user_href 
Get_Status_UserID(user_href)
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = ""
user_href = "https://live.kuaishou.com/u/KGOU5678"
print(Get_Status_UserID(user_href))

运行结果 : {'author_name': '刘鸿运', 'user': 'KGOU5678', 'user_id': '3xuyyti47xptg46'}
```
获取快手用户星座和地址信息
```python
from Kwai import *

# 参数 : kwai_account
Get_Constellation_City(kwai_account)
```
```python
import Kwai
from Kwai import *

Kwai.Cookie_Two = "" # 请注意Cookie_Two 开头是did
# 参数 : kwai_account
Get_Constellation_City("KGOU5678")
运行结果 : {'author_name': '刘鸿运', 'data': {'constellation': '射手座', 'cityName': '广西'}}
```
获取用户的e_tag值
```python
from Kwai import *

# 参数 : user_id
Get_E_Tag(Get_E_Tag)
```
```python
import Kwai
from Kwai import *

Kwai.Cookie = "" 
user_id = Account_ID("fendoushaonianshiwo")
print(Get_E_Tag(user_id))

运行结果 : {'author_name': '刘鸿运', 'e_tag': '1_a/2003292571509223506_xpcwebprofilexxnull0'}
```
快手视频发布评论
```python
from Kwai import *

# 参数 : e_tag,user_id,photo_id,content
Kwai_Comments(e_tag,user_id,photo_id,content)
```
```python
import Kwai
from Kwai import *

# 获取用户的e_tag
e_tag = Get_E_Tag("3x57xtqq9dtxu52")
# 获取视频链接ID和用户ID
id = Get_Video_stream_UserID("https://www.kuaishou.com/short-video/3xj3m4gcsttnnwc?authorId=3x57xtqq9dtxu52&streamSource=profile&area=profilexxnull")
# 发送评论
print(Kwai_Comments(
    e_tag=e_tag['e_tag'],
    user_id=id['data']['user_id'],
    photo_id=id['data']['video_id'],
    content="有才艺"
))

运行结果 : {'author_name': '刘鸿运', 'data': {'time': '2024-05-04 22:11:07', 'commentId': '825207952393', 'content': '有才艺', 'start': True}}
```
快手发送短信验证码 (禁止使用Kwai库盗别人快手账号)
```python
from Kwai import *

# 参数 : phone
Post_Comment(phone)
```
```python
import Kwai
from Kwai import *

phone = 13102597633
print(Post_Comment(13102597633))

运行结果 : {'author_name': '刘鸿运', 'result': True}
```
快手账号登录
```python
from Kwai import *

# 参数 : phone,sms
Post_Login(phone,sms)
```
```python
import Kwai
from Kwai import *

phone = 13102597633
sms = 659075
print(Post_Comment(phone,sms))

# 由于Token 涉及隐私，我就不放自己的了
运行结果 : {'author_name': '刘鸿运', 'data': {'token': ['由于Token涉及我隐私，就不外放了!'], 'user': 1449407088, 'name': '奋斗少年'}, 'is_new_user': False, 'is_login': True}
```
