import time, schedule, random, re, math, requests
from lxml.etree import XPath
from bs4 import BeautifulSoup as bs, SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.expected_conditions import visibility_of_element_located as voel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options 
from datetime import datetime
from multiprocessing import Pool

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
            
import DbConnector as dbconn
import Const

conn = dbconn.connect(Const.DB_HOST, Const.DB_PORT, Const.DB_USER, Const.DB_PW, Const.DB_NAME)

options = Options()
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")
# options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
options.add_experimental_option("detach", True)  
options.add_experimental_option('prefs', prefs)
err = []

BASE_URL = "https://maplestory.nexon.com"

def getHtml(url):
    while True:
        try:
            response = requests.get(url, stream=True, timeout=60)  # 타임아웃 설정 및 응답 스트리밍
            response.raise_for_status()  # 200 이외의 상태 코드에 대한 예외 발생

            soup = bs(response.content, "html.parser")

            with open("output.file", "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            
            break  # 요청 성공 시 루프 종료

        except requests.exceptions.ChunkedEncodingError as e:
            print("ChunkedEncodingError 발생:", e)
            print("다시 시도...")
            print(url)
            time.sleep(2)  # 재시도 전 백오프

        except requests.exceptions.RequestException as e:
            print("요청 실패:", e)
            print(url)
            time.sleep(2)
            # break  # 다른 요청 오류 발생 시 루프 종료

    # html = requests.get(url, stream=True, timeout=30).content
    return soup

def getNoticeWithSoup(data):
    url = f"{BASE_URL}/News/Notice/Inspection?page={data[1]}"
    soup = getHtml(url)
    div = soup.select_one('div.news_board')
    routeUrl = div.find_all('li')[-1].p.a['href']

    try:
        for i in range((data[1] - data[0]) * 10):
            soup2 = getHtml(BASE_URL + routeUrl)

            if id := re.match(r'(.*)\?page(.*)', routeUrl):
                id = str(id.group(1).split('/')[-1])
            else:
                id = str(routeUrl.split('/')[-1])

            title = soup2.select_one('p.qs_title>span').text
            content = soup2.select_one('div.new_board_con')
            _date = soup2.select_one('div.qs_info>p.last').text
            date = _date if _date.count('.') == 2 else datetime.utcnow().strftime('%Y.%m.%d')

            sql = f"INSERT INTO MAPLE_INSPECTION_T (id, title, content, date, worker) VALUES (%s, %s, %s, %s, %s)"
            dbconn.insert(conn, sql, (id, title, content, date, data[2]))
            # print(id, title, content, date, data[2])

            routeUrl = soup2.select_one('span.page_move_btn>a')['href']
    except Exception as ex:
        print(ex)

def getLastNoticePageWithSoup():
    prc = 8
    maxPage = 0

    url = f"{BASE_URL}/News/Notice/Inspection"
    soup = getHtml(url)
    routeUrl = soup.select_one('span.cm_all_next').a['href']

    while True:
        soup2 = getHtml(BASE_URL + routeUrl)
        tmp1 = soup2.select_one('span.cm_all_next').a
        tmp2 = soup2.select_one('span.cm_next').a
        if tmp1.has_attr('href'):
            routeUrl = tmp1['href']
        elif tmp2.has_attr('href'):
            routeUrl = tmp2['href']
        elif len(soup2.select_one('div.news_board').ul.find_all('li')) == 0:
            routeUrl = soup2.select_one('span.cm_prev').a['href']
            break
        else: break

    maxPage = int(re.match(r'(.*)\?page(.*)', routeUrl).group(2)[1:])

    if maxPage > 0:
        remainNum = maxPage % prc
        mx = [math.trunc(maxPage / prc) * (i + 1) for i in range(prc)]
        # mn = [v if len(mx) - 1 == idx else v + 1 for idx, v in enumerate(mx)]
        mn = [v for v in mx]
        mn.pop()
        mn.insert(0, 0)

        _li = [(mn[idx], v + remainNum, f'worker-{idx}') if len(mx) - 1 == idx else (mn[idx], v, f'worker-{idx}') for idx, v in enumerate(mx)]

        pool = Pool(prc)
        pool.map(getNoticeWithSoup, _li)
        pool.close()
        pool.join()
    else:
        return

def getUpdateWithSoup(data):
    url = f"{BASE_URL}/News/Update?page={data[1]}"
    soup = getHtml(url)
    div = soup.select_one('div.update_board')
    routeUrl = div.find_all('li')[-1].p.a['href']

    try:
        for i in range((data[1] - data[0]) * 10):
            soup2 = getHtml(BASE_URL + routeUrl)

            if id := re.match(r'(.*)\?page(.*)', routeUrl):
                id = str(id.group(1).split('/')[-1])
            else:
                id = str(routeUrl.split('/')[-1])

            # id = str(re.match(r'(.*)\?page(.*)', routeUrl).group(1).split('/')[-1])
            title = soup2.select_one('p.qs_title>span').text
            content = soup2.select_one('div.new_board_con')
            _date = soup2.select_one('div.qs_info>p.last').text
            date = _date if _date.count('.') == 2 else datetime.utcnow().strftime('%Y.%m.%d')

            sql = f"INSERT INTO MAPLE_UPDATE_T (id, title, content, date, worker) VALUES (%s, %s, %s, %s, %s)"
            dbconn.insert(conn, sql, (id, title, content, date, data[2]))
            # print(id, title, content, date, data[2])

            routeUrl = soup2.select_one('span.page_move_btn>a')['href']
    except Exception as ex:
        print(ex)

def getLastUpdatePageWithSoup():
    prc = 8
    maxPage = 0

    url = f"{BASE_URL}/News/Update"
    soup = getHtml(url)
    routeUrl = soup.select_one('span.cm_all_next').a['href']

    while True:
        soup2 = getHtml(BASE_URL + routeUrl)
        tmp1 = soup2.select_one('span.cm_all_next').a
        tmp2 = soup2.select_one('span.cm_next').a
        if tmp1.has_attr('href'):
            routeUrl = tmp1['href']
        elif tmp2.has_attr('href'):
            routeUrl = tmp2['href']
        elif len(soup2.select_one('div.update_board').ul.find_all('li')) == 0:
            routeUrl = soup2.select_one('span.cm_prev').a['href']
            break
        else: break

    maxPage = int(re.match(r'(.*)\?page(.*)', routeUrl).group(2)[1:])

    if maxPage > 0:
        remainNum = maxPage % prc
        mx = [math.trunc(maxPage / prc) * (i + 1) for i in range(prc)]
        # mn = [v if len(mx) - 1 == idx else v + 1 for idx, v in enumerate(mx)]
        mn = [v for v in mx]
        mn.pop()
        mn.insert(0, 0)

        _li = [(mn[idx], v + remainNum, f'worker-{idx}') if len(mx) - 1 == idx else (mn[idx], v, f'worker-{idx}') for idx, v in enumerate(mx)]

        pool = Pool(prc)
        pool.map(getUpdateWithSoup, _li)
        pool.close()
        pool.join()
    else:
        return


if __name__ == '__main__':
    print('절대 실행 x')
    pass
    # getLastNoticePageWithSoup()
    # getLastUpdatePageWithSoup()