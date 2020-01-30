from django.urls import path
from .views import (
    nts_home,
    getcert,
    del_ctacert,
    get_idpw,
    set_ctaid,
    set_bsid,
    get_ctaidpw,
    get_bsidpw,
    nts_z1001
)

app_name = 'nts'
urlpatterns = [
    path('', nts_home, name='ntshome'),
    path('ctaid/', set_ctaid, name='set_ctaid'),
    path('bsid/', set_bsid, name='set_bsid'),
    path('ctapw/', get_ctaidpw, name='get_ctaidpw'),
    path('bspw/', get_bsidpw, name='get_bsidpw'),
    path('getcert/', getcert, name='getcert'),
    path('del/', del_ctacert, name='cert-delete'),
    path('idpw/', get_idpw, name='get_idpw'),
    path('nts_z1001/', nts_z1001, name='nts_z1001'),
]
