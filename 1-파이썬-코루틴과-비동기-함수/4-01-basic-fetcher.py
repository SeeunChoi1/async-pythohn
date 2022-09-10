import requests
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    # 웹에서 데이터를 받아오는 코드
    urls = [
        "https://naver.com",
        "https://google.com",
        "https://instagram.com",
    ] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 13.681
