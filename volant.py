import requests
import json


def baidu_upload(path):
    data = {"media": open(path, 'rb')}
    url = 'https://baijiahao.baidu.com/builderinner/api/content/file/upload'   
    user_dic=json.loads(json.dumps(requests.post(url, files=data).json()))
    print(user_dic["ret"]["https_url"])


def toutiao_upload(path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"
    }
    data = {
        "photo": open(path, 'rb+')
    }
    url = 'https://mp.toutiao.com/upload_photo/?type=json'
    res = requests.post(url, files=data, headers=headers).json()
    print(json.dumps(res, indent=4))


def niutu_upload(path):
    headers = {'authority': 'www.niupic.com'}
    files = {'image_field': open(path, 'rb')}
    url = 'https://www.niupic.com/index/upload/process'
    res = requests.post(url, files=files, headers=headers).json()
    print(json.dumps(res, indent=4))

def niutu_upload(path):
    headers = {'authority': 'www.niupic.com'}
    files = {'image_field': open(path, 'rb')}
    url = 'https://www.niupic.com/index/upload/process'
    res = requests.post(url, files=files, headers=headers).json()
    print(json.dumps(res, indent=4))

def smms_upload(path):
    headers = {'Authorization': 'EY3EuuVxGCoPyjLgL6WW2MfLKTyZUwmH'}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
    print(json.dumps(res, indent=4))

if __name__ == "__main__":
    toutiao_upload(r"‪d://桌面//lbcnzyyexcelzz.webp")
