from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from store.models import Product


def say_hello(request):
    # query_set = Product.objects.all()
    #
    # for product in query_set:
    #     print(product)
    return render(request, 'hello.html',{'name':'Asher'} )


