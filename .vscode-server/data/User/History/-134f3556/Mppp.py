from django.shortcuts import render
from .models import render

# Create your views here.
def register(request):
    if request. method == "GET" :
        return render(request, 'register/register.html')
    elif request. method == "POST" :
        print(request.POST)
        print(type(request.POST))
        memberID = request. POST['memberID']
        password = request. POST['password1']
        name = request.POST['username']
        email = request.POST['email']

        memberregister = Member(
            memberID = memberID,
            password = password,
            name = name,
            email = email,
        )
        memberregister.save()
        return render(request, 'register/register.html')