from django.urls import path
from .views import (
    nts_home,
    getcert,
    del_ctacert,
    get_idpw
)

app_name = 'nts'
urlpatterns = [
    path('', nts_home, name='ntshome'),
    path('getcert/', getcert, name='getcert'),
    path('del/', del_ctacert, name='cert-delete'),
    path('idpw/', get_idpw, name='get_idpw'),
]
