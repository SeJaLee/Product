import sys
import io
from bs4 import BeautifulSoup
import requests
import time

# def job():
#     sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#     sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

URL = "https://store.sony.co.kr/handler/ViewProduct-Start?productId=92487311"
# URL ="https://store.sony.co.kr/handler/ViewProduct-Start?productId=92487212&intcmp=Main_%EC%9D%B8%EA%B8%B0%EC%A0%9C%ED%92%8804_210531_WH-1000XM4"

# Session 생성
while True:
    with requests.Session() as s:

        # HTTP GET Request: requests대신 s 객체를 사용한다.
        req = s.get(URL)

        if req.status_code == requests.codes.ok: # 만일 서버가 정상적으로 열려있다면
            soup = BeautifulSoup(req.text, 'html.parser') # soup변수에 html 저장
            stock_a = soup.find("a", class_="buy")

            if stock_a == None: # 재고 없을 경우
                a=1


            else: # 재고 있을 경우
                print("구매 가능")


                def post_message(token, channel, text):
                    response = requests.post("https://slack.com/api/chat.postMessage",
                                             headers={"Authorization": "Bearer " + token},
                                             data={"channel": channel, "text": text})

                myToken = "xoxb-1983717984807-2004666170148-aulLTLn0C3yqPLscmPsV1MYK"
                post_message(myToken, "#product_alarm", "WF-1000MX4 입고됨!!")

