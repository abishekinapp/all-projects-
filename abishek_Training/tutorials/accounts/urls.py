


from django.conf.urls import url
from . import views  # the '.' means it will serch in the project folder and fid out the file


urlpatterns =[
    url(r'^$',views.home)

]