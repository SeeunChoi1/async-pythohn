import requests
import time
import os
import threading


def fetcher(session, url):
    # 프로세스는 각각의 id인 P-id를 가지고 있음
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    # 웹에서 데이터를 받아오는 코드
    urls = ["https://google.com", "https://apple.com"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 16.96
