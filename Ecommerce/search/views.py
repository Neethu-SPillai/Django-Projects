from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from shop.models import Product
# Create your views here.
def searchresult(request):
    products=None
    query=None
    if request.method=="POST":
        query=request.POST.get('q')
        if query:
            products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})

