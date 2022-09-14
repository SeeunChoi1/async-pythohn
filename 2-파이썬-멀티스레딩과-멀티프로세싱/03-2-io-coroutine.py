import aiohttp
import time
import asyncio
import os
import threading


# 코루틴
async def fetcher(session, url):
    # 프로세스 stamp
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text()


async def main():
    # 웹에서 데이터를 받아오는 코드
    urls = ["https://naver.com", "https://google.com"] * 50

    async with aiohttp.ClientSession() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 3.16
