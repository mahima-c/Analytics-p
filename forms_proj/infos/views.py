from django.shortcuts import render

from .forms import *
from .model import Info
from django.http import JsonResponse



# Create your views here.
def info_add_views(request):
    form=InfoModelForm(request.POST or None)
    data={}
    if request.method=='POST':
        print('works')
        name=request.POST.get('name')
        description=request.POST.get('description')
        Info.objects.create(name=name,description=description)
        data['name']=name
        date['description']=description
        return JsonResponse(date,safe=False)

    context={
        'form':form
    }    
    return render(request,'infos/main.html',context=context)

