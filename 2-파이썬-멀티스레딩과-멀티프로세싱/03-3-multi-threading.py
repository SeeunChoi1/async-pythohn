from concurrent.futures import ThreadPoolExecutor
import requests
import time
import os
import threading

# request를 import받아 비동기를 구현했지만 그러지 못하는 상황이거나
# 이미 만들어진 코드를 비동기적으로 수정해야하는 상황이라면?


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    # 웹에서 데이터를 받아오는 코드
    urls = ["https://google.com", "https://apple.com"] * 50

    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))  # (실행하고자 하는 함수, 파라미터)
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 2.70
