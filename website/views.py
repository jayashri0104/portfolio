from django.shortcuts import render,HttpResponse
from .models import Blog


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

     return render(
        request,
        template_name="website/index.html"
    
     )
   
        

        
        

            
    
