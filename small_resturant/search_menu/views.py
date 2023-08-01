from django.shortcuts import render,redirect
from . import models as md
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def home(request):
    last_page=0
    usr=request.session.get("user_name", None)
    if usr !=None:
        user=User.objects.get(username=usr)
        logined='Logged in as '+usr
        history=md.search_history.objects.filter(user_id=user).order_by("-ID").values()[:5]
    else:
        logined="Not Logged in"
        history=""
    if 'Search_return' in request.POST:
        items=list(md.menu_items.objects.all().order_by('-Count').values())
        query=request.POST['Search_return']
        if len(query)>3:
            start=int(request.POST['Page'])
            a=md.menu_details.objects.filter(Item__contains=query).order_by("-Resturant__True_rating").values(
                'ID','Item','Item_det','Price','Resturant','Resturant__Resturant_Name','Resturant__Rating','Resturant__No_of_votes')[start:start+10]
            # print(a)
            if usr !=None:
                search=md.search_history(Search_item=query,user_id=user)
                search.save()
            if len(a)<10:
                last_page=1
            return render(request,'index.html',context={'data':a,'Query':query,'Page':start+10,'last_page':last_page,'items':items[:1000],'history':history,'login':logined})
        query=""
        return render(request,'index.html',context={'Query':query,'Page':0,'history':history,'login':logined})
    else:
        items=list(md.menu_items.objects.all().order_by('-Count').values())
        query=""
        return render(request,'index.html',context={'Query':query,'Page':0,'items':items[:1000],'history':history,'login':logined})
def signup(request):
    if 'user_name' in request.session:
        return redirect(home)
    if 'user_id' in request.POST:
        print(request.POST)
        user_name=request.POST['User_name']
        email=request.POST['Email']
        password=request.POST['Password']
        password2=request.POST['Password2']
        if password!=password2:
            return render(request,'signup.html',context={'Msg':'Passwords dont match'})
        user = User.objects.create_user(username=user_name,email=email,password=password)
        user.save()
        request.session['user_name']=user_name
        return redirect(home)
    else:
        return render(request,'signup.html',context={'Msg':'Create Account'})

    
def login(request):
    if 'user_name' in request.session:
        return redirect(home)
    if 'user_id' in request.POST:
        user_name=request.POST['User_name']
        password=request.POST['Password']
        user = authenticate(username=user_name, password=password)
        print(user)
        if not user:
            return render(request,'login.html',context={'Msg':'Invalid Password'})
        else:
            request.session['user_name']=str(user)
            return redirect(home)
    else:
        return render(request,'login.html',context={'Msg':'login'})
def logout(request):
    try:
        del request.session["user_name"]
    except KeyError:
        pass
    return redirect(login)