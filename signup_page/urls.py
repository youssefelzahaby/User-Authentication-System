from django.urls import path
from . import views

urlpatterns = [

    path('',views.main,name='signup'),
    path('success',views.success,name='succ')
]
