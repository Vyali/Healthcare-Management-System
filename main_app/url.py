from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.index),
url(r'^bookbed$',views.bookbed),
url(r'^doctor',views.doctor),

]
