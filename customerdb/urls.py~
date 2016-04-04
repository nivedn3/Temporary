"""customerdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cd.views import sellerlogin,bargain,sellersignup,front,sellergcm,sellercategory,advt,feed,customer2seller,s2c,sel_conf,cus_conf,item,decline,userdata,updateuser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^front/',front),
    url(r'^login/',sellerlogin),
    url(r'^signup/',sellersignup),
    url(r'^gcmid/',sellergcm),
    url(r'^category/',sellercategory),
    url(r'^c2s/',customer2seller),
    url(r'^s2c/',s2c),
    url(r'^cus_conf/',cus_conf),
    url(r'^clink/',item),
    url(r'^decline/',decline),
    url(r'^userdata/',userdata),
    url(r'^updateuser/',updateuser),
    url(r'^adv/',advt),
    url(r'^feed/',feed),
    url(r'^bargain/',bargain),
    url(r'^selconf/',sel_conf),

 #   url(r'^simg/',simg),    


]
