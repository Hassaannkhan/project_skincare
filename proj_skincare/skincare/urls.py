from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="skincare-home"), 
    path("skincareform/", views.skincareform ,name='skincare-skincareform'),
    # path('med/',views.med_list,name='skincare-med')
]