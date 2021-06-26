from bs4 import BeautifulSoup
import requests
import time


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",

                             data={
                                 'Content-Type': 'application/x-www-form-urlencoded',
                                 'token': token,
                                 'channel': channel,
                                 'text': text})


URL = "https://store.sony.co.kr/handler/ViewProduct-Start?productId=92487311"
myToken = "xoxb-1983717984807-2004666170148-3xZmECauP7Vg6rGGgr4OTTKH"

# Session 생성
while True:
    with requests.Session() as s:
        # HTTP GET Request: requests대신 s 객체를 사용한다.
        req = s.get(URL)
        if req.status_code == requests.codes.ok: # 만일 서버가 정상적으로 열려있다면
            soup = BeautifulSoup(req.text, 'html.parser') # soup변수에 html 저장
            stock_a = soup.find("a", class_="buy")

            # 재고 없을 경우
            if stock_a == None:
                print("재고 없음")
                post_message(myToken, "product_alarm", "WF-1000MX4 재고없음")

            # 재고 있을 경우
            else:
                print("구매 가능")
                post_message(myToken, "product_alarm", "WF-1000MX4 입고됨!!")
        else:
            print("a")

