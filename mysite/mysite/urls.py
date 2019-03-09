"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from learn import  views as learn_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',learn_view.index),
    path(r'add/',learn_view.add,name="add"), #地址栏以add/?a=1&b=2方式进行接收参数
    path(r'add/<int:a>/<int:b>/',learn_view.add2,name="add2"), #add/1/2/格式进行参数接收
    path(r'add_new/<int:a>/<int:b>/',learn_view.add2_new),
    path(r'default',learn_view.default,name="defalut"), #跳转到default页面

]
