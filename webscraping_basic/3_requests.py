import requests
res = requests.get("http://google.com")
# print("응답코드 : ", res.status_code) # 200이면 정상
res.raise_for_status()
"""
# 문제가 생겼을때 확인법 1번
if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 ",res.status_code, "]")

# 문제가 생겼을때 확인법 2번   --> 보통 2번을 씀
res.raise_for_status()
print("웹 스트래핑을 진행합니다.")
"""
print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
