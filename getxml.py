#coding=utf-8

import http.cookiejar
import urllib
import urllib.request
import urllib.parse
import re
import sys
'''模拟登录'''

CaptchaUrl = "http://www.cnvd.org.cn/jcaptcha/jpeg/imageCaptcha?id=1529473521"
PostUrl = "http://www.cnvd.org.cn/user/doLogin"
# 验证码地址和post地址
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# 将cookies绑定到一个opener cookie由cookielib自动管理
username = 'oxhu119@sina.com'
password = 'plmm1234'
# 用户名和密码
picture = opener.open(CaptchaUrl).read()
# 用openr访问验证码地址,获取cookie
local = open('d:/image.jpg', 'wb')
local.write(picture)
local.close()
# 保存验证码到本地
SecretCode = input('输入验证码： ')
# 打开保存的验证码图片 输入
postData = {
'email': username,
'password': password,
'myCode': SecretCode,
}
# 根据抓包信息 构造表单

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '54',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'www.cnvd.org.cn',
'Origin': 'http://www.cnvd.org.cn',
'Referer': 'http://www.cnvd.org.cn/user/login',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
# 根据抓包信息 构造headers
data = urllib.parse.urlencode(postData).encode(encoding='UTF8')
# 生成post数据 ?key1=value1&key2=value2的形式
request = urllib.request.Request(PostUrl, data, headers)
# 构造request请求
try:
    response = opener.open(request)
    # TODO 20180620 download xmlfile
    for step in range(0,999):
        sharedata = urllib.request.Request('http://www.cnvd.org.cn/shareData/download/' + step, data, headers)
        local = open('d:/', 'wb')
        local.write(picture)
        local.close()
    # result = response.read()
    # print(result)
# 打印登录后的页面
except urllib.request.HTTPError as e:
    print(e.code)
# 利用之前存有cookie的opener登录页面