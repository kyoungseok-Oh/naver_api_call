import requests

def call_api(keyword):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&display=100"
    res = requests.get(url, headers={
        "X-Naver-Client-Id": "pop_N16zSQ5CfKCqSAWA",
        "X-Naver-Client-Secret": "nTey074Ju3"
    })

    print(res)
    r = res.json()
    print(len(r['items']))

if __name__ == '__main__':
    call_api("교대역 병원")
