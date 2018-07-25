


from django.conf.urls import url
from . import views  # the '.' means it will serch in the project folder and fid out the file
from django.contrib.auth.views import login

urlpatterns =[
    url(r'^$',views.home)
    url(r'^ login/$',login,{'template_name':'account/login.htlm'})

]
  
