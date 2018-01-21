# coding:utf-8
import requests
import json
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from concurrent import futures

'''使用方法
python2或者3都可以
安装库
pip install bs4 requests selenium lxml
先去运行phone.py获取手机号。根据需要来.
如果运行第二种请确保下载了浏览器驱动对应版本并设置路径
运行前检查号码库文件是哪个。然后运行


'''


def one(phone_num):
    session = requests.Session()
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
              'Cookie': 'channel=cW11dG1fc291cmNlPWJhaWR1c2VvJnFtdXRtX2t3PQ; Um-C=CeVD4IlDCqBkNySv4kaDIdsg5FyAGu3zmecgJOIMjIVEzRjETgGBjomJZfOqTfig+TJhQM9Jcvc9fNDSnUP+eFTke+niL6kn51FrUSEqH3q2suQeE9YLfr17jNsImExCmeF+yZ4UGCQ=; Um-W=B6sL7dT5XyADRudiZYeS4nChaUHqQuGT82MhZgzz78vnDqP8Z7FaV30C4vnuMLAUPNiOvrW3q7rXxXnc8nQ6OlnYNGz9iBLnNNFUwLE6yH3I4HTWxohLw+M94ZUqmAnIfdIzIdUZ8jaciqfjIGy5QQVn0oMXhe2+7eQfrAhEuJhI4j+/BgmBoLsmrDMJ0q5G; Um-R=pgxoW1yakl9bU0fwAG0n7yPaYEbUOpCNu5JPagYfdt0gjm0mwG0QYRmd3HWs7YcJ3+xwGUQ+7IgyfScZPrVDytuzUkg8AbVW4VLpSOaEt8q2GvVH9mvcMBXWiE9E4Xf7pDLUNamAEJrVluofj8YeclwNG3tEqByAhP5Mtmvm+f9KZ4hedeal28O6OQFfHvm+nzOGQNubBevppGuFP/hwDIJM2dn7Y6sVxe9jvhmjpuiOknpeGHZfPnnZ+llUwNG9akwf14A99yiHYS6vHCwNNhKihVpD+wVrEAaBfeU7twzLD9jdtQHKcSqDr7oZlz/DBKIzgyvaDBksZVlZTPFaGxKby/3nw1i+mRfd2EvYEpp55/j3ShUKFCS3R4ps+PVYbLzIPi+srBl0C2HcZR4rf3EuSoRz6Mad4++QLw/RqhBLeso1D0+XS6vdiq1oeyyR; _ga=GA1.2.651950911.1513427333; _gid=GA1.2.1265022952.1513427333; gr_user_id=322f8b22-763d-4686-9e6f-56c2594b4da1; gr_session_id_a370b353401c73da=5787c8d9-924d-42f0-9270-873502f1458f; nTalk_CACHE_DATA={uid:kf_9575_ISME9754_guestA63EB54F-086E-CF,tid:1513427381548889}; NTKF_T2D_CLIENTID=guestA63EB54F-086E-CFAD-11AB-5F4D2D2C4991; SSOTICKET=; SSOCHILDTICKET=; SSOEXPIRES=; SSOTHRESHOLD=; a9a68f4fefd3b693f10be4a89799dc48=79a47bab347b4f119bea030ba0293e6b; OFCaptchaControl=OFCaptchaControl69d2cad9-8911-4f05-b849-e64f5815eb7f; PHPSESSID=4D5DD8A92832FB5CB062C62B14C11AD2; _gat=1',
              'Host': 'www.1000.com',
              'X-Requested-With': 'XMLHttpRequest'}
    with session:
        payload = {
            ''
            'mobile': '{}'.format(phone_num),
            'qmext': '',
            'refer': 'https://www.baidu.com/link?url=RtleTEkTazCCeODUJbDd9211UkE2OEkzHS8sNwcJwWe&wd=&eqid=e1e08d0400046b22000000055a35117a'
        }

        url = "https://www.1000.com/reg/check/mobile"
        res = session.post(url, headers=header, params=payload).content
        result = json.loads(res)
        print(result)
        print(result["msg"])
        try:
            if result["rescode"] == 201:
                save_file(phone_num)
        except:
            pass


def two(phone_num):
    login_url = "https://www.1000.com/reg"
    driver = webdriver.Firefox(executable_path="/Users/maxpain/Documents/driver/geckodriver")
    #
    # driver = webdriver.Chrome(executable_path="/Users/maxpain/Documents/driver/chromedriver")

    driver.get(login_url)
    elem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/div[2]/div/div/input')
    time.sleep(0.5)
    driver.implicitly_wait(15)
    elem.send_keys("{}".format(phone_num))
    time.sleep(1)
    driver.find_element_by_id('send_code').click()
    content = driver.page_source.encode("utf-8")
    time.sleep(0.5)
    soup = BeautifulSoup(content, "lxml")
    try:
        message = soup.find('div', {'id': 'err_tip'}).text.strip()
        if message:
            if u"已被注册" in message:
                save_file(phone_num)
                time.sleep(1)

    except:
        pass


def get_phone():
    with open("new.txt", 'r') as rp:
        phones = rp.read()
    phone_list = phones.split("\n")
    return phone_list


def save_file(file):
    with open("qianmi.txt", 'a') as wp:
        wp.write(file+"\n")


if __name__ == '__main__':
    phones = get_phone()
    # # for i in phones:
    # #     two(i)  # 自动化方式
    # #     one(i)  # 接口
    # #     time.sleep(1)
    #
    with futures.ThreadPoolExecutor(32) as executor:
        executor.map(one, phones)
    # s = {"code":10100,"msg":"\u8be5\u624b\u673a\u53f7\u5df2\u88ab\u6ce8\u518c","data":[]}
    # print(s["msg"])
