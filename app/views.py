from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def topic_insert(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic is inserted succesfully')
    return render(request,'topic_insert.html')

def insert_webpage(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        topic=request.POST['topic']
        n=request.POST['n']
        url=request.POST['url']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url,email=em)[0]
        WO.save()
        return HttpResponse('insert webpage is successfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LOA=Webpage.objects.all()
    d={'topics':LOA}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST.get('date')
        WO=Webpage.objects.get(name=name)
    
        AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('insert_access is successfully')
    return render(request,'insert_access.html',d)
def retrieve_data(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()
        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)

def checkbox(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'checkbox.html',d)

def radio(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'radio.html',d)