import os
import sys
import json
import time
from datetime import datetime
import pandas as pd
import win32com.client
import binascii  # excel Hexadecimal to file(binary)

iftCertdll = win32com.client.Dispatch("iftCoreEngine.iftGate")
iftServicedll = win32com.client.Dispatch("iftWinExAdapter.clsAdapter")


Data = "Hellow World!!"
# 인포텍 공인인증서 정보 모듈 함수


def get_cert_info():
    req_str = ""
    res_str = iftCertdll.getUserCert(req_str)  # json str
    cert_info = json.loads(res_str)      # json to dic
    if cert_info['cert_nm'] == "":              # 취소 버튼 클릭시
        return None
    return cert_info

# 현재시간(초까지) '2019-12-04 11:47:22' https://hoy.kr/I5NZW


def get_now():
    now = datetime.now()
    now_format = '%Y-%m-%d %H:%M:%S'
    strNow = now.strftime(now_format)
    return strNow
