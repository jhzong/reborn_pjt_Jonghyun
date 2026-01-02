from django.shortcuts import render
from django.http import HttpResponse
from restaurants.models import Restaurant
from django.core.paginator import Paginator

def reslist(request):
    qs = Restaurant.objects.all()
    page=int(request.GET.get('page',1))# 없으면 default=1
    paginator=Paginator(qs,20)#20개씩 자르기
    list_qs=paginator.get_page(page)

    context={'list':list_qs,'page':page}
    return render(request,'restaurants/reslist.html',context)

def resview(request):
    return render(request,'restaurants/resview.html')