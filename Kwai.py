"""

开发者 : 刘鸿运
 年龄 :   18
介绍  : 此库是由刘鸿运开发，因为刘鸿运和前任程羽闹掰了，
刘鸿运账号被程羽全部拉黑，特此编写快手API库，
功能 : 关注,取消关注,猜你喜欢,举报,获取用户信息,
获取推荐视频,账号是否被拉黑,快手号转用户ID,无视快手号跳页面等等.

"""
import json
import re
import time
import datetime
import requests
import jsonpath
from urllib.parse import quote


# 设置Search_Key查询当前自己账号信息
Search_Key = ""
# Cookie 适用于基本功能
Cookie = ""
# Cookie_Two 适用于直播
Cookie_Two = ""
# AI小快账号
AI_BOT_ID = "3xvgq9jpiayug3s"

def fendou():

    return Cookie

def fendou_two():
    return Cookie_Two
# 作者介绍
def Auto_User(name,age,text,*pake):

    name = "刘鸿运"
    age = 18
    text = """此库是由刘鸿运开发，因为刘鸿运和前任程羽闹掰了，
              刘鸿运账号被程羽全部拉黑，特此编写快手API库，可以轻松
              实现快手基本功能数据获取，PC端和APP端快手数据采集,被采集人情绪
              分析，被采集人喜欢看的视频采集等等。
    """

    print("*" * 35 + "欢迎使用刘鸿运开发的快手API库" + "*" * 35)

    print(f"""
              作者 : {name}
              年龄 : {age}
              介绍 : {text}
    """)
# Auto_User(name=(),age=(),text=())

# 获取单个用户内容
def Search_Message(user_id):

    key = quote(str(user_id))


    headers = {
        'Content-Type' : 'application/json',
        'Cookie' : fendou(),
        'Host' : 'www.kuaishou.com',
        'Origin' :'https://www.kuaishou.com',
        'Referer' : f'https://www.kuaishou.com/profile/{key}',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionProfilePhotoList",
        "variables": {
            "userId": f"{key}",
            "pcursor": "",
            "page": "profile"
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    # user_id
    user_id_json = jsonpath.jsonpath(repone.json(),"$..id")
    # user_name
    user_name = jsonpath.jsonpath(repone.json(),"$..name")
    # headerurl
    headerurl = jsonpath.jsonpath(repone.json(),"$..headerUrl")

    return {'author_name':"刘鸿运",'data':{
        'user_id' : user_id_json[0],
        'user_name' : user_name[0],
        'headerurl' : headerurl[0]
    }}

# 获取搜索用户全部内容
def Search_Message_All(search_id,*page):

    key = quote(str(search_id))

    app = []

    headers = {
        'Content-Type' : 'application/json',
        'Cookie' : fendou(),
        'Host' : 'www.kuaishou.com',
        'Origin' :'https://www.kuaishou.com',
        'Referer' : f'https://www.kuaishou.com/search/video?searchKey={key}',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionSearchPhoto",
        "variables": {
            "keyword": key,
            "pcursor": str(page),
            "page": "search"
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    res = repone.json()['data']['visionSearchPhoto']['feeds']

    for result in res :

        # name
        name = result['author']['name']
        # id
        id = result['author']['id']
        # headerUrl
        headerUrl = result['author']['headerUrl']
        # following
        following = result['author']['following']
        app.append({f'name':name,'id':id,'following':following,'headerUrl':headerUrl})

    return {'author':"刘鸿运",'data':app}

# 检测账号是否被拉黑
def Search_Black(user_id):

    key = quote(str(user_id))

    headers = {
        'Content-Type' : 'application/json',
        'Cookie' : fendou(),
        'Host' : 'www.kuaishou.com',
        'Origin' :'https://www.kuaishou.com',
        'Referer' : f'https://www.kuaishou.com/search/video?searchKey={key}',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionSearchPhoto",
        "variables": {
            "keyword": user_id,
            "pcursor": "",
            "page": "search"
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    ts = jsonpath.jsonpath(repone.json(),'$..id')[0]

    if len(jsonpath.jsonpath(repone.json(),'$..id')[0]) > 0 :

        return {'author_name':"刘鸿运",'user_black':False} # 没有被拉黑
    else:
        return {'author_name':"刘鸿运",'user_black':True} # 已经被拉黑

# 可能感兴趣的人
def Search_Interested():

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/myFollow',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "likeUserData",
        "variables": {},
        "query": "fragment linkResult on RelationSearchUserResult {\n  result\n  pcursor\n  prsid\n  users {\n    visitorBeFollowed\n    userSex\n    isFollowing\n    userName\n    userId\n    userText\n    verified\n    extra {\n      reason\n      reason_value\n      openUserName\n      __typename\n    }\n    headUrl\n    userReason\n    __typename\n  }\n  __typename\n}\n\nquery likeUserData($pcursor: String, $prsid: String, $pageSize: Int) {\n  likeUser(pcursor: $pcursor, prsid: $prsid, pageSize: $pageSize) {\n    ...linkResult\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    js = repone.json()['data']['likeUser']

    # 推荐 猜你喜欢快手号的数量
    number = js['pcursor']

    # 获取用户列表
    user = js['users']

    data = {

    }

    app = []

    for k in user :

        # 快手用户性别
        Sex = ''

        if str(k['userSex']) == 'M' :
            Sex = '男生'
        elif str(k['userSex']) == 'F' :
            Sex = '女生'
        else :
            Sex = '没有设置性别'

        # 快手用户名
        Kwai_Name = k['userName']
        # 快手用户ID
        Kwai_ID = k['userId']
        # 快手用户简介
        Kwai_Text = k['userText']
        # 类型
        Kwai_Link = k['userReason']
        # 头像地址
        Kwai_Header = k['headUrl']


        if len(Kwai_Text) > 0 :
            app.append({'Name':Kwai_Name,'ID':Kwai_ID,'Text':Kwai_Text,'Link':Kwai_Link,'Header':Kwai_Header})
        else:
            app.append({'Name':Kwai_Name,'ID':Kwai_ID,'Text':'用户太懒了,没有设置简介','Link':Kwai_Link,'Header':Kwai_Header})

    data['author_name'] = '刘鸿运'
    data['Number'] = number
    data['User'] = app

    return data

# 推荐视频
def Recommendation():


    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/?isHome=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "brilliantDataQuery",
        "variables": {
            "semKeyword": "",
            "semCrowd": "",
            "utmSource": "",
            "utmMedium": "",
            "page": "home",
            "photoId": ""
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantDataQuery($pcursor: String, $semKeyword: String, $semCrowd: String, $utmSource: String, $utmMedium: String, $page: String, $photoId: String, $utmCampaign: String, $webPageArea: String) {\n  brilliantData(pcursor: $pcursor, semKeyword: $semKeyword, semCrowd: $semCrowd, utmSource: $utmSource, utmMedium: $utmMedium, page: $page, photoId: $photoId, utmCampaign: $utmCampaign, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    rs = repone.json()['data']['brilliantData']['feeds']

    data = {

    }

    app = []

    for content in rs :

        # 视频标题
        title = content['photo']['caption']
        # 视频源地址
        photourl = content['photo']['photoH265Url']
        # 视频点赞量
        likeCount = content['photo']['likeCount']
        # 视频播放量
        viewCount = content['photo']['viewCount']
        # 视频收藏量
        realLikeCount = content['photo']['realLikeCount']

        app.append({'title':title,'linkCount':likeCount,'viewCount':viewCount,'realLikeCount':realLikeCount,'photoUrl':photourl})

    data['author_name'] = "刘鸿运"
    data['Content'] = app

    return data

# 随机推荐视频
def Randomly_Recommend_Videos():

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/?isHome=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "brilliantDataQuery",
        "variables": {
            "semKeyword": "",
            "semCrowd": "",
            "utmSource": "",
            "utmMedium": "",
            "page": "home",
            "photoId": ""
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantDataQuery($pcursor: String, $semKeyword: String, $semCrowd: String, $utmSource: String, $utmMedium: String, $page: String, $photoId: String, $utmCampaign: String, $webPageArea: String) {\n  brilliantData(pcursor: $pcursor, semKeyword: $semKeyword, semCrowd: $semCrowd, utmSource: $utmSource, utmMedium: $utmMedium, page: $page, photoId: $photoId, utmCampaign: $utmCampaign, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    rs = repone.json()['data']['brilliantData']['feeds']

    data = {

    }

    app = []

    for content in rs :

        # 视频标题
        title = content['photo']['caption']
        # 视频源地址
        photourl = content['photo']['photoH265Url']
        # 视频点赞量
        likeCount = content['photo']['likeCount']
        # 视频播放量
        viewCount = content['photo']['viewCount']
        # 视频收藏量
        realLikeCount = content['photo']['realLikeCount']

        app.append({'title':f'{title}','linkCount':f'{likeCount}','viewCount':f'{viewCount}','realLikeCount':f'{realLikeCount}','photoUrl':f'{photourl}'})

    data['author_name'] = "刘鸿运"
    data['Content'] = app[0]

    return data


# 推荐关注用户
def Recommended_Followers():

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/?isHome=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "brilliantDataQuery",
        "variables": {
            "semKeyword": "",
            "semCrowd": "",
            "utmSource": "",
            "utmMedium": "",
            "page": "home",
            "photoId": ""
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantDataQuery($pcursor: String, $semKeyword: String, $semCrowd: String, $utmSource: String, $utmMedium: String, $page: String, $photoId: String, $utmCampaign: String, $webPageArea: String) {\n  brilliantData(pcursor: $pcursor, semKeyword: $semKeyword, semCrowd: $semCrowd, utmSource: $utmSource, utmMedium: $utmMedium, page: $page, photoId: $photoId, utmCampaign: $utmCampaign, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    rs = repone.json()['data']['brilliantData']['feeds']

    data = {

    }

    app = []

    for content in rs :


        # 用户ID
        User_ID = content['author']['id']
        # 用户名
        User_Name = content['author']['name']

        app.append({f'id:{User_ID},name:{User_Name},href:https://www.kuaishou.com/profile/{User_ID}'})

    data['author_name'] = "刘鸿运"
    data['Content'] = app

    return data

# 快手号转用户ID
def Account_ID(kwai_account):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/search/video?searchKey={kwai_account}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "graphqlSearchUser",
        "variables": {
            "keyword": f"{kwai_account}"
        },
        "query": "query graphqlSearchUser($keyword: String, $pcursor: String, $searchSessionId: String) {\n  visionSearchUser(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId) {\n    result\n    users {\n      fansCount\n      photoCount\n      isFollowing\n      user_id\n      headurl\n      user_text\n      user_name\n      verified\n      verifiedDetail {\n        description\n        iconType\n        newVerified\n        musicCompany\n        type\n        __typename\n      }\n      __typename\n    }\n    searchSessionId\n    pcursor\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    # 用户ID
    user_id = jsonpath.jsonpath(repone.json(),'$..user_id')

    return user_id[0]

# 快手账号举报用户
def Report_Account(User_ID,Content,*ju):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{User_ID}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "ReportSubmitMutation",
        "variables": {
            "targetId": f"{User_ID}",
            "reportType": 2,
            "page": "PROFILE",
            "reportItem": 214, # 214 : 其他违规(默认214) 203 : 政治信息不全  215 : 传播低俗色情内容
            "reportDetail": f"{Content}", # 举报内容
            "reportedUserId": f"{User_ID}",
            "extraPhotoId": ""
        },
        "query": "mutation ReportSubmitMutation($targetId: String, $reportType: Int, $page: String, $reportItem: Int, $reportDetail: String, $reportedUserId: String, $extraPhotoId: String) {\n  visionReportSubmit(targetId: $targetId, reportType: $reportType, page: $page, reportItem: $reportItem, reportDetail: $reportDetail, reportedUserId: $reportedUserId, extraPhotoId: $extraPhotoId) {\n    result\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    if jsonpath.jsonpath(repone.json(),'$..result')[0] == 1 :
        return {'author_name':"刘鸿运","data":{
            'user_id':User_ID,'content':Content,
            'mode':ju[0],'return':'true'
        }} # 举报成功
    else:
        return {'author_name': "刘鸿运", "data": {
            'user_id': User_ID, 'content': Content,
            'mode': ju[0], 'return': 'false'
        }}  # 举报失败

# 快手关注
def Follow(user_id):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionFollow",
        "variables": {
            "touid": f"{user_id}",
            "ftype": 1,
            "followSource": 1
        },
        "query": "mutation visionFollow($touid: String, $ftype: Int, $followSource: Int, $expTag: String) {\n  visionFollow(touid: $touid, ftype: $ftype, followSource: $followSource, expTag: $expTag) {\n    result\n    followStatus\n    hostName\n    error_msg\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    value = ""
    user_name = Search_Message(user_id)['data']['user_name']
    if Search_Black(user_id) == False :
        value = "没有被拉黑"
    else:
        value = "账号被拉黑"

    # 如果搜索账号成功就关注
    if jsonpath.jsonpath(repone.json(),'$..followStatus')[0] == 1 :
        return {'author_name':"刘鸿运","data":{
            "id":user_id,
            'name':user_name,
            'following' : value, # 账号是否被拉黑
            'follow_status' : True # 关注状态
        }} # 关注成功
    else:
        return {'author_name': "刘鸿运", "data": {
            "id": user_id,
            'name': user_name,
            'following': value,
            'follow_status': False
        }} # 关注失败

# 快手取消关注
def Cancel_Follow(user_id):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionFollow",
        "variables": {
            "touid": user_id,
            "ftype": 2,
            "followSource": 1
        },
        "query": "mutation visionFollow($touid: String, $ftype: Int, $followSource: Int, $expTag: String) {\n  visionFollow(touid: $touid, ftype: $ftype, followSource: $followSource, expTag: $expTag) {\n    result\n    followStatus\n    hostName\n    error_msg\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    value = ""
    user_name = Search_Message(user_id)['data']['user_name']

    if Search_Black(user_id) == False :
        value = "没有被拉黑"
    else:
        value = "账号被拉黑"

    # 如果搜索账号成功取消关注
    if jsonpath.jsonpath(repone.json(),'$..followStatus')[0] == 1 :
        return {'author_name':"刘鸿运","data":{
            "id":user_id,
            'name':user_name,
            'following' : value, # 账号是否被拉黑
            'close_follow' : True # 关注状态
        }} # 取消关注成功
    else:
        return {'author_name':"刘鸿运","data":{
            "id":user_id,
            'name':user_name,
            'following' : value, # 账号是否被拉黑
            'close_follow' : False # 关注状态
        }} # 取消关注失败

# 检测快手是否关注用户
def Judging_Attention(user_id):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionProfile",
        "variables": {
            "userId": f"{user_id}"
        },
        "query": "query visionProfile($userId: String) {\n  visionProfile(userId: $userId) {\n    result\n    hostName\n    userProfile {\n      ownerCount {\n        fan\n        photo\n        follow\n        photo_public\n        __typename\n      }\n      profile {\n        gender\n        user_name\n        user_id\n        headurl\n        user_text\n        user_profile_bg_url\n        __typename\n      }\n      isFollowing\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    # 快手号转ID
    user = Account_ID(user_id)

    # 获取到用户名
    value = Search_Message(user)['data']['user_name']
    # 获取到用户ID
    values = Search_Message(user)['data']['user_id']

    info = ''
    # 账号是否被拉黑
    if Search_Black(user) == False:
        info = "没有被拉黑"
    else:
        info = "账号被拉黑"

    # 判断用户是否关注此人
    if jsonpath.jsonpath(repone.json(),'$..isFollowing')[0] == False :
        return {
            'author_name' : '刘鸿运','data':{
                'user_name' : value ,
                'user_id' : values,
                'user_black' : info,
                'user_following' : False
            }
        } # 没有关注
    else:
        return {
            'author_name' : '刘鸿运','data':{
                'user_name' : value ,
                'user_id' : values,
                'user_black' : info,
                'user_following' : True
            }
        } # 关注了

# 当前账号信息
def Get_Auto_User():

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{Search_Key}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "userInfoQuery",
        "variables": {},
        "query": "query userInfoQuery {\n  visionOwnerInfo {\n    id\n    name\n    avatar\n    eid\n    userId\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    return {'author_name':"刘鸿运","data":{
        'id' : jsonpath.jsonpath(repone.json(),'$..id')[0],
        'name' : jsonpath.jsonpath(repone.json(),'$..name')[0],
        'eid' : jsonpath.jsonpath(repone.json(),'$..eid')[0],
        'user_id' : jsonpath.jsonpath(repone.json(),'$..userId')[0],
    }}

# 获取视频评论信息
def Get_Video_Mssage(user_id):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/short-video/{user_id}?utm_source=video&utm_medium=video&utm_campaign=video',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "commentListQuery",
        "variables": {
            "photoId": user_id,
            "pcursor": ""
        },
        "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    return repone.json()

# 获取视频评论数量
def Get_Video_Number(user_id):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/short-video/{user_id}?utm_source=video&utm_medium=video&utm_campaign=video',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "commentListQuery",
        "variables": {
            "photoId": user_id,
            "pcursor": ""
        },
        "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url, headers=headers, json=params)

    return jsonpath.jsonpath(repone.json(),"$..commentCount")[0]

# 获取快手视频总数量
def Get_Video_Number(user_id):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionProfile",
        "variables": {
            "userId": user_id
        },
        "query": "query visionProfile($userId: String) {\n  visionProfile(userId: $userId) {\n    result\n    hostName\n    userProfile {\n      ownerCount {\n        fan\n        photo\n        follow\n        photo_public\n        __typename\n      }\n      profile {\n        gender\n        user_name\n        user_id\n        headurl\n        user_text\n        user_profile_bg_url\n        __typename\n      }\n      isFollowing\n      __typename\n    }\n    __typename\n  }\n}\n"
    }


    repone = requests.post(url,headers=headers,json=params)

       # 如果视频数量大于0
    if int(jsonpath.jsonpath(repone.json(),"$..photo_public")[0]) > 0  :
        return {'author_name':'刘鸿运','data':{
            'video_number':jsonpath.jsonpath(repone.json(),"$..photo_public")[0]
        }}
    else:
        return {'author_name': '刘鸿运', 'data': {
            'video_number': '该用户没有发布任何作品'
        }}


# 快手视频 作者自制研究版本判断
def Justice_Judgment(value,*values) :

    if value == True : # 判断为真
        return values # 执行结果
    else:
        return False  # 判断为假 返回False

# 获取评论区评论 半正式测试
def Get_Comments(user_id,video_id):

    app0 = []
    app1 = []

    data = {}

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "commentListQuery",
        "variables": {
            "photoId": video_id,
            "pcursor": ""
        },
        "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    res = repone.json()['data']['visionCommentList']

    # 获取视频评论总数量
    commentCount = res['commentCount']

    red = repone.json()['data']['visionCommentList']['rootComments']
    cd = repone.json()["data"]["visionCommentList"]["rootComments"][0]["subComments"]
    count = -1
    for rootComments in red :

        count += 1

        # user_id
        user_id_info = rootComments['authorId']
        # user_name
        user_name = rootComments['authorName']
        # content
        content = rootComments['content']
        # timestamp
        timestamp = rootComments['timestamp']

        # 假设时间戳是以毫秒为单位的
        timestamp_milliseconds = timestamp

        # 将时间戳转换为秒，因为datetime模块中的时间戳是以秒为单位的
        timestamp_seconds = timestamp_milliseconds / 1000.0

        # 创建一个datetime对象
        dt = datetime.datetime.fromtimestamp(timestamp_seconds)

        # value
        value = dt.strftime('%Y-%m-%d %H:%M:%S')

        # 如果用户评论有回复内容
        if len(cd) > 0 :

            # 循环取内容
            for subComments in red[count]['subComments'] :
                # user_id
                user_id_info = subComments['authorId']
                # user_name
                user_name = subComments['authorName']
                # content
                content = subComments['content']
                # timestamp
                timestamp = subComments['timestamp']
                # replyToUserName
                replyToUserName = subComments['replyToUserName']

                # 假设时间戳是以毫秒为单位的
                timestamp_milliseconds = timestamp

                # 将时间戳转换为秒，因为datetime模块中的时间戳是以秒为单位的
                timestamp_seconds = timestamp_milliseconds / 1000.0

                # 创建一个datetime对象
                dt = datetime.datetime.fromtimestamp(timestamp_seconds)

                # value
                value = dt.strftime('%Y-%m-%d %H:%M:%S')

                # 将评论回复内容添加
                app0.append({'user_id':user_id_info,
                                'user_name':user_name,
                                'content':content,
                                'time':value,
                                'replyToUserName':replyToUserName})
        # 将评论内容添加
        app1.append({'user_id': user_id_info,
                    'user_name': user_name,
                    'content': content,
                    'time': value})

        data['author_name'] = "刘鸿运"
        data['Video_Number'] = commentCount
        data['message'] = {'content':app1,'reply_content':app0}

    return data

# 快手个人主页链接取用户ID
def Get_User_ID(user_href):
    match = re.search(r'/profile/([^/?#]+)', user_href)
    if match:
        return {'author_name': '刘鸿运', 'user_id':match.group(1)}
    else:
        return False  # 没有解析到内容

# 处理快手视频链接取出视频ID和用户ID
def Get_Video_User_ID(user_href):

    # 使用正则表达式匹配问号及其左右两边的内容
    match = re.search(r'https://www.kuaishou.com/short-video/(.*?)\?.*?(.*)', user_href)
    if match :
        return {'author_name':'刘鸿运','data':{'video_id':match.group(1),'user_id':str(match.group(2))[8:]}}
    else :
        return False # 没有解析到内容

# 处理快手视频同城链接取出视频ID和用户ID
def Get_Video_stream_UserID(user_href):
    match = re.search(r'/short-video/([^?&]+)\?authorId=([^&]+)', user_href)
    if match :
        return {'author_name':'刘鸿运','data':{'video_id':match.group(1),'user_id':match.group(2)}} # str(match.group(2))[8:]
    else :
        return False # 没有解析到内容

# 跳转用户个人账户链接
def Get_User_Href(user_id):
    Get_User_Href
    if len(user_id) > 0 :
        return {'author_name':"刘鸿运",'message':f"https://www.kuaishou.com/profile/{user_id}"}
    else:
        return False # 请输入用户ID

# 下载快手举报视频所需要参数
def Download_Ju_Video():

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        # 视频ID 和 用户ID
        'Referer': f'https://www.kuaishou.com/short-video/3x2gji4i4rbhi6m?userId=3x2c7683mjqy6i9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionReportMenuMutation",
        "variables": {
            "reportType": 1,
            "page": "DETAIL"
        },
        "query": "mutation visionReportMenuMutation($reportType: Int, $page: String) {\n  visionReportMenu(reportType: $reportType, page: $page) {\n    result\n    menuInfo {\n      symbol\n      symbolName\n      reportItems {\n        value\n        desc\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    with open('快手视频举报.json','w',encoding='utf-8') as file :
        file.write(repone.text)
    return {'author_name':"刘鸿运","download":True} # 下载成功

# 获取快手账号登录IP地址
def Get_IP_Host():

    url = 'http://sdkoptedge.chinanetcenter.com/sdk/v2?return_client_ip=1&url_type=1&qtype=v4'
    repone = requests.get(url)

    res = repone.json()['client_ip']

    try : # 如果捕捉的IP城市不太精准的报错的话就执行下面异常
        headers = {
            'Host' : 'www.ipshudi.com',
            'Referer' : 'https://www.ip138.com/',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

        urls = f'https://www.ipshudi.com/{res}.htm'

        repones = requests.get(urls,headers=headers)

        resds = re.compile(r'<span>(.*?) <a href="https://www.liantu.cn/bendi/xingtai/"  rel="nofollow" target="_blank">(.*?)</a> (.*?)</span>')
        resd = resds.findall(repones.text)

        return {'author_name':"刘鸿运","data":{
            'ip' : res,
            'city' : str(resd[0][0]+resd[0][1]+resd[0][2])
        }}
    except IndexError :

        headers = {
            'Host' : 'www.ipshudi.com',
            'Referer' : 'https://www.ip138.com/',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

        urls = f'https://www.ipshudi.com/{res}.htm'

        repones = requests.get(urls,headers=headers)

        resds = re.compile(r'<span>(.*?) <a href="https://www.liantu.cn/bendi/xingtai/"  rel="nofollow" target="_blank">(.*?)</a> (.*?)</span>')
        resd = resds.findall(repones.text)

        return {'author_name':"刘鸿运","data":{
            'ip' : res,
            'city' : str(resd[0][0]+resd[0][1])
        }}

# 快手是否开直播
def Live_Streaming_Status(kwai_account):

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Cookie': fendou(),
        'Host': 'live.kuaishou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = f'https://live.kuaishou.com/u/{kwai_account}'

    repone = requests.get(url,headers=headers)

    res = re.compile(r"<span data-v-15f23ba5>(.*?)</span>")
    if len(res.findall(repone.text)) > 0 and res.findall(repone.text)[0] == "主播尚未开播，可以观看其他直播" :
        return {'author_name':"刘鸿运","start":False} # 未开直播
    else:
        return {'author_name': "刘鸿运", "start": True}  # 正在开直播

# 快手直播链接取快手号 自动转用户ID
def Get_Status_UserID(user_href):

    username = re.search(r'/u/([^/?#]+)', user_href)

    if username:
        value = Account_ID(username.group(1))
        return {'author_name': "刘鸿运", 'user': username.group(1), "user_id": value}
    else:
        return {'author_name': "刘鸿运", 'user': username.group(1), "user_id": None} # 未能找到快手号的用户ID

# 获取快手用户星座和地址信息
def Get_Constellation_City(kwai_account):

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Cookie': fendou_two(),
        'Host': 'live.kuaishou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = f'https://live.kuaishou.com/live_api/baseuser/userinfo/sensitive?principalId={kwai_account}'

    repone = requests.get(url,headers=headers)

    # 判断作者是否设置地址信息
    if len(jsonpath.jsonpath(repone.json(),'$..cityName')) > 0 :
        return {
            'author_name': "刘鸿运", 'data': {
                'constellation': jsonpath.jsonpath(repone.json(), "$..constellation")[0],
                'cityName' : jsonpath.jsonpath(repone.json(),'$..cityName')[0]
            }
        }
    else:
        return { # 作者没有配置地址信息
            'author_name': "刘鸿运", 'data': {
                'constellation': jsonpath.jsonpath(repone.json(), "$..constellation")[0],
                'cityName' : "作者没有设置地址",
            }
        }

# 获取用户的E_Tag值
def Get_E_Tag(user_id):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionProfilePhotoList",
        "variables": {
            "userId": f"{user_id}",
            "pcursor": "",
            "page": "profile"
        },
        "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)


    return {'author_name':"刘鸿运","e_tag":jsonpath.jsonpath(repone.json(),"$..expTag")[0]}

# 快手视频发布评论
def Kwai_Comments(e_tag,user_id,photo_id,content,start):

    headers = {
        'Accept' : '*/*',
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/short-video/{photo_id}?authorId={user_id}&streamSource=profile&area=profilexxnull',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionAddComment",
        "variables": {
            "photoId": photo_id,
            "photoAuthorId": user_id,
            "content": content,
            "expTag": e_tag
        },
        "query": "mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    time_token = jsonpath.jsonpath(repone.json(),"$..timestamp")[0]

    # 假设时间戳是以毫秒为单位的
    timestamp_milliseconds = time_token

    # 将时间戳转换为秒，因为datetime模块中的时间戳是以秒为单位的
    timestamp_seconds = timestamp_milliseconds / 1000.0

    # 创建一个datetime对象
    dt = datetime.datetime.fromtimestamp(timestamp_seconds)

    # value
    value = dt.strftime('%Y-%m-%d %H:%M:%S')

    res = repone.json()

    # 发布评论判断成功
    if jsonpath.jsonpath(repone.json(),"$..status")[0] == "success" and start == True:

        # 把评论的ID保存下来
        with open("commentId.text",'w',encoding='utf-8')as file:
            file.write(str(res["data"]["visionAddComment"]))

        return {
            'author_name' : "刘鸿运",
            'data' : {
                'time' : value,
                'commentId' : res["data"]["visionAddComment"]["commentId"],
                'content' : res["data"]["visionAddComment"]["content"],
                'start' : True # 发布评论成功
            }
        }
    elif jsonpath.jsonpath(repone.json(),"$..status")[0] == "success" and start == False:
        return {
            'author_name' : "刘鸿运",
            'data' : {
                'time' : value,
                'commentId' : res["data"]["visionAddComment"]["commentId"],
                'content' : res["data"]["visionAddComment"]["content"],
                'start' : True # 发布评论成功
            }
        }
    else:
        return {
            'author_name' : "刘鸿运",
            'data' : {
                'time' : value,
                'commentId' : jsonpath.jsonpath(repone.json,'$..commentId')[0],
                'content' : jsonpath.jsonpath(repone.json(),"$..content")[0],
                'start' : False # 发布评论信息失败
            }
        }

# 快手发送登录验证码
def Post_Comment(phone):

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': fendou(),
        'Host': 'id.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/new-reco',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://id.kuaishou.com/pass/kuaishou/sms/requestMobileCode'

    params = {
        'sid' : 'kuaishou.server.web',
        'type' : 53,
        'countryCode' : '+86' , # 中国大陆
        'phone' : phone,
        'account' : '',
        'ztIdentityVerificationType' : '',
        'ztIdentityVerificationCheckToken' : '',
        'channelType' : 'UNKNOWN',
        'encryptHeaders' : ''
    }

    repone = requests.post(url,headers=headers,params=params)

    if repone.json()['result'] == 1 :
        return {
            'author_name' : '刘鸿运',
            'result' : True
        } # 发送验证码成功
    else:

        return {
            'author_name' : '刘鸿运',
            'result' : False
        } # 发送验证码失败

# 快手登录拿已登录过的快手账号数据
def Post_Login(phone,sms):

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': fendou(),
        'Host': 'id.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/new-reco',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://id.kuaishou.com/pass/kuaishou/login/mobileCode'

    params = {
        'countryCode' : '+86', # 中国大陆通用
        'phone' : phone ,
        'sid' : 'kuaishou.server.web',
        'createId' : 'true',
        'smsCode' : sms,
        'setCookie' : 'true',
        'channelType' : 'UNKNOWN' ,
        'encryptHeaders' : ''
    }

    repone = requests.post(url,headers=headers,params = params)

    # 检测快手登录账号是1个还是2个
    if len(jsonpath.jsonpath(repone.json(),"$..userInfos")) == 2 :
        # 判断快手是否登录成功
        if repone.json()['result'] == 100110031 :
            return {
                'author_name' : "刘鸿运",
                'data' : {
                    'token' : jsonpath.jsonpath(repone.json(),"$..multiUserToken"),
                    'user' :repone.json()["userInfos"][0]["userId"],
                    'name' :repone.json()["userInfos"][0]["name"],
                    'user_two': repone.json()["userInfos"][1]["userId"],
                    'name_two': repone.json()["userInfos"][1]["name"],
                },
                'is_new_user' : repone.json()["isNewUser"],
                'is_login' : True # 成功登录，拿到登录账号数据
            }
        else:
            return {
                'author_name': "刘鸿运",
                'is_login': False  # 登录失败，未拿到登录账号数据
            }
    elif len(jsonpath.jsonpath(repone.json(),"$..userInfos")) == 1 :
        # 判断快手是否登录成功
        if repone.json()['result'] == 100110031:
            return {
                'author_name': "刘鸿运",
                'data': {
                    'token': jsonpath.jsonpath(repone.json(), "$..multiUserToken"),
                    'user': repone.json()["userInfos"][0]["userId"],
                    'name': repone.json()["userInfos"][0]["name"],
                },
                'is_new_user': repone.json()["isNewUser"],
                'is_login': True  # 成功登录，拿到登录账号数据
            }
        else:
            return {
                'author_name': "刘鸿运",
                'is_login': False  # 登录失败，未拿到登录账号数据
            }

# 判断快手账号是否人机 人机特征 1.0 研究版本 研究人 : 刘鸿运
def Judging_Human_Machine(user_id):

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/profile/{user_id}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionProfile",
        "variables": {
            "userId": user_id,
        },
        "query": "query visionProfile($userId: String) {\n  visionProfile(userId: $userId) {\n    result\n    hostName\n    userProfile {\n      ownerCount {\n        fan\n        photo\n        follow\n        photo_public\n        __typename\n      }\n      profile {\n        gender\n        user_name\n        user_id\n        headurl\n        user_text\n        user_profile_bg_url\n        __typename\n      }\n      isFollowing\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    # 有作品 不是人机
    if int(jsonpath.jsonpath(repone.json(),"$..photo_public")[0]) > 0 :

        return {
            'author_name' : "刘鸿运",
            'user_name' : jsonpath.jsonpath(repone.json(),"$..user_name")[0],
            'user_id' : user_id,
            "user_fan" : jsonpath.jsonpath(repone.json(),"$..fan")[0], # 粉丝数量
            'man-machine' : False # 不是人机

        }
    elif int(jsonpath.jsonpath(repone.json(),"$..photo_public")[0]) == 0 and int(jsonpath.jsonpath(repone.json(),"$..fan")[0]) > 100: # 粉丝数量判断人机特征

        return {
            'author_name' : "刘鸿运",
            'user_name' : jsonpath.jsonpath(repone.json(),"$..user_name")[0],
            'user_id' : user_id,
            "user_fan" : jsonpath.jsonpath(repone.json(),"$..fan")[0], # 粉丝数量
            'man-machine' : True # 是人机
        }

# 获取快手视频标题
def User_Video_Title(user_id,video_id):

    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Cookie' : fendou(),
        'Host' : 'www.kuaishou.com',
        'Referer' : f'https://www.kuaishou.com/short-video/{video_id}?authorId={user_id}&streamSource=find&area=homexxbrilliant',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = f'https://www.kuaishou.com/short-video/{video_id}?authorId={user_id}&streamSource=profile&area=profilexxnull'

    params = {
        'authorId' : user_id,
        'streamSource' :'profile',
        'area' : 'profilexxnull'
    }

    repone = requests.get(url,headers=headers,params=params)

    res = re.compile(r'<title>(.*?)</title>')

    return {
        'author_name' : "刘鸿运",
        "title" : res.findall(repone.text)[0]
    }

# 快手视频标签播放量
def Get_Label_Now(label_name):

    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Cookie' : fendou(),
        'Host' : 'www.kuaishou.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    url = f'https://www.kuaishou.com/hashtag/{label_name}?source=1'

    params = {
        'source' : 1
    }

    repone = requests.get(url,headers=headers,params=params)

    res = re.compile(r'<div class="info-num" data-v-85b0c5e6> (.*?) </div>')

    return {
        'author_name' : "刘鸿运",
        'data' : {
            'label_name' : label_name ,
            'label_count' : res.findall(repone.text)[0]
        }
    }

# 获取快手用户一级ID
def Kwai_One_User_ID(kwai_account):

    headers = {
        'Accept' : 'application/json, text/plain, */*',
        'Content-Type' : 'application/json;charset=UTF-8',
        'Cookie' : fendou(),
        'Host' : 'pay.ssl.kuaishou.com',
        'Origin' : 'https://pay.ssl.kuaishou.com',
        'Referer' : 'https://pay.ssl.kuaishou.com/pay'
    }

    url = 'https://pay.ssl.kuaishou.com/payAPI/k/pay/userInfo'

    params = {
        "id": kwai_account
    }

    repone = requests.post(url,headers=headers,json=params)

    return {
        'author_name' : "刘鸿运",
        'data' : {
            'kwai_account' : kwai_account,
            'id' : jsonpath.jsonpath(repone.json(),"$..userId")[0]
        }
    }

# 快手评论区回复
def Post_Reply_Comment(user_id,video_id,message,reply_id,reply_userid,e_tag):

    headers = {
        'Accept' : '*/*',
        'Content-Type' : 'application/json',
        'Cookie' : fendou(),
        'Host' : 'www.kuaishou.com',
        'Origin' : 'https://www.kuaishou.com',
        'Referer' : f'https://www.kuaishou.com/short-video/{video_id}?authorId={user_id}&streamSource=find&area=homexxbrilliant'
    }

    url = 'https://www.kuaishou.com/graphql'

    params = {
        "operationName": "visionAddComment",
        "variables": {
            "photoId": video_id,
            "photoAuthorId": user_id,
            "content": message,
            "replyToCommentId": reply_id,
            "replyTo": reply_userid,
            "expTag": e_tag
        },
        "query": "mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"
    }

    repone = requests.post(url,headers=headers,json=params)

    return repone.json()

# 调用快手 AI小快解答 (半缺代码，你们自己研究吧)
def AI_Search(Search_Message,user_id,photo_id,CommentId,e_tag,*times):

    headers = {
        'Content-Type': 'application/json',
        'Cookie': fendou(),
        'Host': 'www.kuaishou.com',
        'Origin': 'https://www.kuaishou.com',
        'Referer': f'https://www.kuaishou.com/short-video/3x7hhj4fwnnjbh9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    # 如果账号关注了AI小快
    if Judging_Attention(AI_BOT_ID) == True :

        url = "https://www.kuaishou.com/graphql"

        # 以下视频ID是奋斗少年快手视频的
        params = {
            "operationName": "visionAddComment",
            "variables": {
                "photoId": photo_id, # 视频ID
                "photoAuthorId": user_id, # 用户ID
                "content": Search_Message, # 回复内容
                "replyToCommentId": CommentId, # 评论总ID
                "replyTo": '3xvgq9jpiayug3s', # 回复的用户ID
                "expTag": e_tag
            },
            "query": "mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"
        }

        repone = requests.post(url,headers=headers,json=params)

        # 判断时间
        if times[0] > 0 :
            time.sleep(times[0])
            headers_values = {
                'Content-Type': 'application/json',
                'Cookie': fendou(),
                'Host': 'www.kuaishou.com',
                'Origin': 'https://www.kuaishou.com',
                'Referer': f'https://www.kuaishou.com/short-video/3x7hhj4fwnnjbh9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }

            urls = "https://www.kuaishou.com/graphql"

            paramsd = {
                "operationName": "commentListQuery",
                "variables": {
                    "photoId": photo_id, # 视频ID
                    "pcursor": ""
                },
                "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      authorLiked\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        authorLiked\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
            }

            repones = requests.post(urls,headers=headers_values,json=paramsd)

            res = repones.json()


            return repones.json()

        else:
            time.sleep(2) # 默认2秒

    else:
        return False # 没有关注AI小快，无法使用功能