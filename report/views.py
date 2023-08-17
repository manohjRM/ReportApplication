from report.forms import ReportForm
from report.models import customers
from django.shortcuts import get_object_or_404, redirect, render
#from django.

def index(request):
    company = customers.objects.all()
    context = {
        'company' : company
    }
    return render(request, 'index.html', context=context)

def add_customer(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = ReportForm()
        return render(request, 'add_customer.html', {'form':form})

def edit_customer(request, pk):
    company = get_object_or_404(customers, pk=pk)

    if request.method == "POST":

        form = ReportForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReportForm(instance=company)
        return render(request, 'edit_customer.html', {'form':form})

def del_customer(request, pk):
    customers.objects.filter(id=pk).delete()
    company = customers.objects.all()
    context = {
        'company': company
    }
    return render(request, 'index.html', context)