from fake_useragent import UserAgent

ua = UserAgent()
headers={"User-Agent":ua.random}

if __name__ == '__main__':
    print(headers)