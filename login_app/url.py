from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^login/$',views.login),
url(r'^register/',views.register),
url(r'^registring_user/$',views.register_users, name ='register_users'),
url(r'^user_detail_form/$',views.user_detail_form, name='user_detail_form'),
url(r'^logging_in/$',views.logging_in, name='logging_in'),
url(r'^post_details/$',views.post_details,name='post_details'),
#url(r'^post_url/',views.register_users, name = "register_users")

]
