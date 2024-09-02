from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'index.html')

balance = 1000
count = 0
def check_balance(request):
    global count 
    global balance
    date = datetime.today().date()
    time = datetime.today().time()
    count += 1
    return render(request,'balance.html',{'count':count,'balance':balance,'date':date,'time':time})

def deposit(request):
    global balance
    
    if request.method == 'POST':
        amount = request.POST.get('amt')
        if amount is None:
            return HttpResponse('Amount field is required.')
        try:
            amount = int(amount)
        except ValueError:
            return HttpResponse('Enter a numeric value')
        if amount > 0:
            balance += amount
            return render(request,'deposit.html',{'mes':'Deposit Successful : INR ','dep':amount})
        else:
            return HttpResponse(f'Invalid Amount. Amount should be greater than Zero!!!')
    else:
        return render(request,'deposit.html')
    
def withdraw(request):
    global balance
    if request.method == 'POST':
        amount = request.POST.get('amt')
        if amount is None:
            return HttpResponse('Amount field is required.')
        try:
            amount = int(amount)
        except ValueError:
            return HttpResponse('Enter a numeric value')
        if balance >= amount:
            if amount > 0:
                balance -= amount
                return render(request,'withdraw.html',{'mes':'Withdraw Successfull : INR ','wd':amount,'available':'Available Balance : INR ','ab':balance})
            else:
                return HttpResponse(f'Invalid Amount. Amount should be greater than Zero!!!')
        else:
            return render(request,'withdraw.html',{'insufficicent':'Insufficient Balance : INR ','balance':balance})
    return render(request,'withdraw.html')