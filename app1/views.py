from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    details={"name":"Shri",
             'age': 22,
             'Gender':'Male'}
    
    return render(request,'index.html',context=details)