#from django.http import HttpResponse
from django.shortcuts import render
from members.models import member

def homepage(request, *args, **kwargs):
   # return HttpResponse("Hello World")
   member.objects.create()
   queryset = member.objects.all()
   my_title = "Swim Club matey"
   my_context = {
       
       "page_title": my_title,
       "members_count": queryset.count()
       
   }
   return render(request, 'home.html', my_context)

def about(request, *args, **kwargs):
   # return HttpResponse("About SCP")
    return render(request, 'about.html')

