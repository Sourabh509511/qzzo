from django.shortcuts import render,redirect
from django.views import View
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.crypto import get_random_string
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


# Create your views here.
class welcome(View):
    def get(self,request):
        return render(request,'home.html')


class authentication(View):
    def get(self,request):
        return render(request,'home.html')

    def post(self,request):
        image=request.POST.get('image')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        age=request.POST.get('age')
        uniqueid=request.POST.get('un')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if len(uniqueid) ==0:
            uniqueid=get_random_string(6)

        if pass1==pass2 and len(pass1)>=8:
            user=User.objects.create_user(Image=image,First_name=firstname,Last_name=lastname,Age=age,Unique_id=uniqueid,Email=email,password=pass1)
            user.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('welcome')
        messages.error(request,"Password must be same in both fields and password should be greater then 8 letters")
        return redirect('welcome')

class LoginView(TokenObtainPairView):
    def post(self,request):
        serializer = MyTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        # user= authenticate(username=request.data["Email"], password=request.data["password"])
        login(request,user)
        messages.success(request,f"Successfully logged In as {user}")
        user_data=User.objects.get(Email=request.data['Email'])
        return render(request,'home.html',{'data':user_data})

# class loginView(View):
#     def post(self,request):
#         loginusername=request.POST.get('username')
#         loginpassword=request.POST.get('password')
#         if user is not None:
#             login(request,user)
#             messages.success(request,f"Successfully logged In as {user}")
#             user_data=User.objects.get(Email=loginusername)
#             return render(request,'home.html',{'data':user_data})
#         messages.error(request,"Invalid Credentials!!!")
#         return redirect("welcome")

class logoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Successfully logged out")
        return redirect("/")
