from django.shortcuts import render

def home(request):
   context = {
           'user': request.user,
           'request':request,
      }
   return render(request,'socialauth/home.html',context)