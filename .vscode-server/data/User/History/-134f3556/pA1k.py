from django.shortcuts import render, redirect
from .models import Member

def login(request):
    if request. method == "GET" :
        return render(request, 'login/login.html')
    elif request. method == "POST" :
        memberID = request. POST['memberID']
        password = request. POST['password']
        try:
            check = Member.objects.get(memberID=memberID)
        except:
            check = False

        data_dic = {}
        if not (memberID and password) :
            data_dic["err"] = '모든 값을 입력해 주세요'

        elif check == False :       
            data_dic["err"] = "등록된 아이디가 없습니다."

        else :
            if password == check.password:
                request.session["user"]=memberID
                return redirect("/")
                #data_dic["err"]="로그인 되었습니다."

            else:
                data_dic["err"] = "비밀번호가 잘못되었습니다."
           
        return render(request, 'login/login.html', data_dic)



# 홈 페이지 뷰
#def index(request):
    # 로그인 상태를 확인하고 홈 페이지를 반환
#    if 'user' in request.session:
#        return render(request, 'home/index.html')  # 로그인된 사용자가 있으면 홈 페이지
#    else:
#        return redirect('login')  # 로그인되지 않은 사용자는 로그인 페이지로 리다이렉트


#여기서부터 새로 생성된 부분
def home(request):
    user_data = {}
    user_data["user_id"] = request.session.get("user")  # 세션에서 "user" 값을 가져옴
    print(user_data)
    print(type(user_data))
    return render(request, 'home/index.html', user_data)  # 'home/index.html'에 전달


# 여기까지가 끝
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
        check = Member.objects.filter(memberID = memberID) 
        print(check)
        print(type(check))
        
        if password1 != password2:
            data_dic["err"] = '비밀번호가 일치하지 않습니다.'

        elif not(memberID and password1 and password2 and name and email and subject) :           
            data_dic["err"] = "모든 값을 입력해주세요."

        elif check :
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

