"""BillingPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Billapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('listbill/',views.listBills, name='index'),
    path('addbill/',views.addBills),
    path('addestimatebill/',views.addEstimatedBills),
    path('estimatelistbill/',views.listEstimateBills,name='index1'),
    path('update/<int:pk>/', views.BillingUpdateView.as_view()),
    path('delete/<int:pk>/', views.BillingDeleteView.as_view()),
    path('combinedbill/',views.listCombinedBills,name='index2'),
    path('combinedaddbill',views.addCombinedBills),
    path('estimateupdate/<int:pk>/', views.EstimatedBillUpdateView.as_view()),
    path('estimatedelete/<int:pk>/', views.EstimatedBillDeleteView.as_view()),
    path('combinedupdate/<int:pk>/', views.CombinedBillUpdateView.as_view()),
    path('combineddelete/<int:pk>/', views.CombinedBillDeleteView.as_view()),

]
