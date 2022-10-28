from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

# def htmlforms(request):
#     if request.method =='GET':
#         N=request.GET['UN']
#         P=request.POST['PW']
#         D={'n':N,'p':P}
#         return render(request, 'datahtml.html', D)
#     return HttpResponse
#     #return render(request,'htmlforms.html')

def htmlforms(request):
    if request.method=='POSt':
        N=request.POST['UN']
        P=request.POST['PW']
        D={'n':N,'p':P}
        return render(request, 'datahtml.html', D)
    return render (request,'htmlforms.html')

def insert_topic(request):
    if request.method=='POST':  
        tn=request.POST['tn']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inserted successfully go and check in admin if u want')
    return render(request,'insert_topic.html')
