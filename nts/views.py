from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError 
from django.contrib import messages  # 경고창 https://hoy.kr/kxuTa
from django.http import JsonResponse
from django.views.generic import View

from .models import CtaCert, CtaIdPw, BsIdPw
from scripts.utils import get_cert_info
import json

def nts_home(request):
    template_name = 'nts/nts_home.html'
    ctacert_obj = CtaCert.objects.all()
    ctaidpw_obj = CtaIdPw.objects.all()
    bsidpw_obj = BsIdPw.objects.all()
    context = {
        'ctacert_obj': ctacert_obj,
        'ctaidpw_obj': ctaidpw_obj,
        'bsidpw_obj': bsidpw_obj
        }
    return render(request, template_name, context)

def set_ctaid(request):
    id_cert = request.GET.get('id_cert')
    ctaidpws = CtaIdPw.objects.filter(ctacert_id=id_cert).order_by('ctaid')
    return render(request, 'nts/ctaid_list_options.html', {'ctaidpws': ctaidpws})

def get_ctaidpw(request):
    id_ctaid = request.GET.get('id_ctaid')
    ctaidpw = CtaIdPw.objects.filter(ctaid__exact=id_ctaid)
    print("*"*50, ctaidpw)
    ctaidpw = ctaidpw.values()
    response = {'ctaidpw': ctaidpw}
    print("ctaidpw :", ctaidpw)
    print("response :", response)
    print(type(ctaidpw), type(response))
    return JsonResponse(response, safe=False)

def set_bsid(request):
    id_cert = request.GET.get('id_cert')
    id_ctaid = request.GET.get('id_ctaid')
    bsidpws = BsIdPw.objects.filter(ctacert_id=id_cert).filter(
        ctaidpw_id=id_ctaid).order_by('bsid')
    return render(request, 'nts/bsid_list_options.html', {'bsidpws': bsidpws})


def getcert(request):
    cert_info = get_cert_info()
    if cert_info == None:  # 취소 버튼 클릭시
        msg = "인증서를 선택해 주세요!!!"
        messages.add_message(request, messages.INFO, msg)
        return redirect("/nts/")
    new_cert = CtaCert(**cert_info)
    try:
        new_cert.save()
        msg = f"인증서 [{cert_info['cert_nm']}]가 저장되었습니다!!!"
        messages.add_message(request, messages.INFO, msg)
    except Exception as e:
        msg = f"[{cert_info['cert_nm']}] : 이미 입력된 인증서 입니다!!!"
        messages.add_message(request, messages.INFO, msg)
        return redirect("/nts/")
    return redirect("/nts/")

def del_ctacert(request):
    if request.method == "POST":
        id = request.POST['id']
        obj = get_object_or_404(CtaCert, id=id)
        res = obj.cert_nm
        context = {'object': res}
        obj.delete()
        return JsonResponse(context)
    return redirect("/nts/")


def get_idpw(request):
    
    if request.method == "POST":
        # ctaid = request.POST['agentId']
        
        res_cta_idpw = {
            'ctacert_id': request.POST['certId'],
            'ctaid': request.POST['agentId'],
            'pw': request.POST['agentPw'],
        }
        res_bs_idpw = {
            'ctacert_id': request.POST['certId'],
            'ctaidpw_id': request.POST['agentId'],
            'bsid': request.POST['userId'],
            'pw': request.POST['userPw'],
        }
        if (res_cta_idpw['ctacert_id'] != "" and
            res_cta_idpw['ctaid'] != "" and
            res_cta_idpw['pw'] != ""):
            new_cta_idpw = CtaIdPw(**res_cta_idpw)
            try:
                new_cta_idpw.save()
            except Exception as e:
                print("err : ", e)
                pass

        # ctaid 로 CtaIdPw 테이블 id 값 추출하여 res_bs_idpw 딕셔너리 업데이트
        
        # ctacert_id = CtaIdPw.objects.filter(ctaid__exact=ctaid).values()[0]['ctaid']
        # print(ctacert_id)
        # res_bs_idpw['ctaidpw_id'] = ctacert_id
        
        if (res_bs_idpw['ctacert_id'] != "" and
            res_bs_idpw['ctaidpw_id'] != "" and
            res_bs_idpw['bsid'] != "" and
                res_bs_idpw['pw'] != ""):

            new_bs_idpw = BsIdPw(**res_bs_idpw)
            try:
                new_bs_idpw.save()
            except Exception as e:
                print("err : ", e)
                pass

        response = {
            'res_cta_idpw': res_cta_idpw,
            'res_bs_idpw': res_bs_idpw
        }

    return JsonResponse(response)
