from django.shortcuts import render
from . import models as md
# Create your views here.
def home(request):
    last_page=0
    if 'Search_return' in request.POST:
        items=list(md.menu_items.objects.all().order_by('-Count').values())
        query=request.POST['Search_return']
        if len(query)>3:
            start=int(request.POST['Page'])
            a=md.menu_details.objects.filter(Item__contains=query).order_by("-Resturant__True_rating").values(
                'ID','Item','Item_det','Price','Resturant','Resturant__Resturant_Name','Resturant__Rating','Resturant__No_of_votes')[start:start+10]
            # print(a)
            if len(a)<10:
                last_page=1
            return render(request,'index.html',context={'data':a,'Query':query,'Page':start+10,'last_page':last_page,'items':items[:1000]})
        query=""
        return render(request,'index.html',context={'Query':query,'Page':0})
    else:
        items=list(md.menu_items.objects.all().order_by('-Count').values())
        query=""
        return render(request,'index.html',context={'Query':query,'Page':0,'items':items[:1000]})