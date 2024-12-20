from django.shortcuts import render
from .models import Member

# Create your views here.
def register(request):
    if request. method == "GET" :
        return render(request, 'register/register.html')
    elif request. method == "POST" :
        print(request.POST)
        #print(type(request.POST))
        memberID = request. POST['memberID']
        password1 = request. POST['password1']
        password2 = request. POST['password2']
        name = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject1']

        data_dic = {}

        if password1 != password2:
            data_dic["err"] = '비밀번호가 일치하지 않습니다.'

        else :
            memberregister = Member(
                memberID = memberID,
                password = password1,
                name = name,
                email = email,
                subject1 = subject
            )
            memberregister.save()
        return render(request, 'register/register.html')