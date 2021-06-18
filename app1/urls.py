from django.urls import path
from  . import views

urlpatterns = [
path('code',views.fncode),
path('sample',views.fnsample)   

]
