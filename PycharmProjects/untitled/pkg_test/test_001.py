# _*_ coding:utf-8 _*_
import os
import logging
import urllib
import requests

def test_file():
    data = """这是第一行
    这是第二行
    这是第三行"""

    data = ("这是第一行", "这是第二行", "这是第三行")
    with open("test_01.txt", "w+") as f:
        # data = r"这是第一行"
        # f.write(data)
        # data = r"这是第二行"
        # f.write(data)

        f.writelines(data)
    with open("test_01.txt", "r") as f:
        print(f.tell())
        var = f.read(3)
        while var:
            print(f.tell(), ":", var)
            var = f.read(3)


def test_logging():
    LOG_FORMAT = "[%(levelname)s] %(asctime)s_%(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")


def test_ulrlib():
    var_url = r"http://www.baidu.com"
    rsp = requests.get(var_url)
    print(rsp.status_code)
    print(rsp.encoding)
    print(rsp.apparent_encoding)
    rsp.encoding(rsp.apparent_encoding)
    print(rsp)




if __name__ == "__main__":
    test_ulrlib()
