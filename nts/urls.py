from django.urls import path
from .views import (
    nts_home,
    getcert,
    del_ctacert,
    get_idpw,
    set_ctaid,
    set_bsid,
    get_ctaidpw
)

app_name = 'nts'
urlpatterns = [
    path('', nts_home, name='ntshome'),
    path('ctaid/', set_ctaid, name='set_ctaid'),
    path('bsid/', set_bsid, name='set_bsid'),
    path('ctapw/', get_ctaidpw, name='get_ctaidpw'),
    path('getcert/', getcert, name='getcert'),
    path('del/', del_ctacert, name='cert-delete'),
    path('idpw/', get_idpw, name='get_idpw'),
]
