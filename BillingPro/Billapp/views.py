from django.shortcuts import render,redirect
from django.views.generic import  ListView, UpdateView, DeleteView
from Billapp.forms import BillingForm, EstimatedBillForm, CombinedBillingForm
from Billapp.models import Billing, EstimatedBill, CombinedBilling
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return render(request,'Billapp/index.html')



def listBills(request):
    billlist=Billing.objects.all()
    return render(request,'Billapp/listbill.html',{'billlist': billlist})


def addBills(request):
    form=BillingForm()
    if request.method=='POST':
        form=BillingForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'Billapp/addBills.html',{'form':form})

def listEstimateBills(request):
    estimatedBillList=EstimatedBill.objects.all()
    return render(request,'Billapp/estimatelistbill.html',{'estimatedBillList': estimatedBillList})


def addEstimatedBills(request):
    form= EstimatedBillForm
    if request.method=='POST':
        form=EstimatedBillForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'Billapp/addEstimateBills.html',{'form':form})


def listCombinedBills(request):
    combinedBillList = CombinedBilling()
    return render(request,'Billapp/combinedlistbill.html',{'combinedBillList': combinedBillList})


def addCombinedBills(request):
    form= CombinedBillingForm()
    if request.method=='POST':
        form=CombinedBillingForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'Billapp/combinedBills.html',{'form':form})

class BillingUpdateView(UpdateView):
        model = Billing
        fields = '__all__'
        template_name='Billapp/addBills.html'
        success_url = reverse_lazy('index')


class BillingDeleteView(DeleteView):
        billlist = Billing.objects.all()
        model= Billing
        template_name='Billapp/billing_confirm_delete.html'
        success_url = reverse_lazy('index')


class EstimatedBillUpdateView(UpdateView):
    model = EstimatedBill
    fields = '__all__'
    template_name = 'Billapp/addEstimateBills.html'
    success_url = reverse_lazy('index1')

class EstimatedBillDeleteView(DeleteView):
        estimateBillList = EstimatedBill.objects.all()
        model = EstimatedBill
        template_name = 'Billapp/estimatebill_confirm_delete.html'
        success_url = reverse_lazy('index1')

class CombinedBillUpdateView(UpdateView):
    model = CombinedBilling
    fields = '__all__'
    template_name = 'Billapp/combinedBills.html'
    success_url = reverse_lazy('index2')

class CombinedBillDeleteView(DeleteView):
    combinedBillList = CombinedBilling.objects.all()
    model = CombinedBilling
    template_name = 'Billapp/combinedbill_confirm_delete.html'
    success_url = reverse_lazy('index2')