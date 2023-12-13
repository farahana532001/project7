from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('bhupendra/',bhupendra,name='bhupendra'),
    path('kaaling/',kaaling,name='kaaling'),
]