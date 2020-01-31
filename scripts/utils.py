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

req = '{"appCd": "aitax", "orgCd": "hometax", "svcCd": "Z1001", "loginMethod": "CERT", "agentId": "w15960", "userId": "innotax154", "signCert": "C:\\Users\\김명중\\AppData\\LocalLow\\NPKI\\yessign\\USER\\cn=세무법인이노택스테헤(BizBank)008868520131118188000375,ou=BizBank,ou=SHB,ou=xUse4Esero,o=yessign,c=kr\\SignCert.der", "signPri": "C:\\Users\\김명중\\AppData\\LocalLow\\NPKI\\yessign\\USER\\cn=세무법인이노택스테헤(BizBank)008868520131118188000375,ou=BizBank,ou=SHB,ou=xUse4Esero,o=yessign,c=kr\\SignPri.key", "signPw": "innotax1260!", "agentPw": "1234", "userPw": "dlshxortm14!"}'

def get_cert_info():
    req_str = ""
    res_str = iftCertdll.getUserCert(req_str)  # json str
    cert_info = json.loads(res_str)      # json to dic
    if cert_info['cert_nm'] == "":              # 취소 버튼 클릭시
        return None
    return cert_info

def ift_call2(req_str):
    print(req_str)
    print(">"*100)
    res_str, req_str = iftServicedll.serviceCall2(req_str)
    print("*"*100)
    res_dict = json.loads(res_str)
    print(res_dict)
    return res_dict

# 현재시간(초까지) '2019-12-04 11:47:22' https://hoy.kr/I5NZW
def get_now():
    now = datetime.now()
    now_format = '%Y-%m-%d %H:%M:%S'
    strNow = now.strftime(now_format)
    return strNow


# print(">"*100)
# res_str, req_str = iftServicedll.serviceCall2(req)
# print("*"*100)
# res_dict = json.loads(res_str)
# print(res_dict)
