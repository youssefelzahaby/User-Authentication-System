from django.shortcuts import render
from .models import Sign
# Create your views here.
def main(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        f_name = request.POST.get("f_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        number = request.POST.get("number")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            new_user = Sign(
                gender=gender,
                f_name=f_name,
                username=username,
                email=email,
                number=number,
                password=password,
            )

            new_user.save()
            return render(request, 'todo.html')
        else:
             return render(request, 'signup.html')
    return render(request, 'signup.html')

####################################################################################################33
def success(request):
    return render(request,'todo.html')
