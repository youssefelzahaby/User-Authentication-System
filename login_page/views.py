from django.shortcuts import render
from .models import login
from signup_page.models import Sign
def login_page(request):
    if request.method == "POST":

     username = request.POST.get("username")
     password = request.POST.get("password")
     data=login(username=username,password=password)
     try:
         user = Sign.objects.get(username=username, password=password)


         return render(request, 'todo.html')
     except Sign.DoesNotExist:
         return render(request, 'login.html', )
    return render (request, 'login_page.html')




