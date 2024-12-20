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
        check_id = Member.objects.get(memberID = memberID) 
        
        #if not(memberID and password1 and password2 and name and email and subject1) :           
        #    data_dic["err"] = "모든 값을 입력해주세요."
        #elif check_id:
        #    print(check)
        #    print(check.memberID)
        #    print(check.password)

        #    data_dic["err"] = "이미 등록된 아이디 입니다."
        
        if password1 != password2:
            data_dic["err"] = '비밀번호가 일치하지 않습니다.'

        elif check_id :
            data_dic["err"] = '이미 있는 아이디 입니다.'

        else :
            memberregister = Member(
                memberID = memberID,
                password = password1,
                name = name,
                email = email,
                subject1 = subject
            )
            memberregister.save()
        return render(request, 'register/register.html', data_dic)