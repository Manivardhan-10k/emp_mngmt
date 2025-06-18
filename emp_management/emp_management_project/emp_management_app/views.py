from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Employee
import bcrypt


from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def sample(req):
    return HttpResponse("the app is working properly")



def user_exists(mob=None, user=None, pswrd=None):
    if mob and not (user and pswrd):
        return Employee.objects.filter(contact=mob).first()

    elif user and pswrd and not mob:
        employee = Employee.objects.filter(name=user).first()

        if employee and bcrypt.checkpw(pswrd.encode('utf-8'), employee.password.encode('utf-8')):
            return employee
        else:
            return None


@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        department = request.POST.get("department")
        designation = request.POST.get("designation")
        password = request.POST.get("password")  
        profile_image = request.FILES.get("profile_image")
        
        if user_exists(mob=contact):
            return JsonResponse({"msg": "User already exists with same mobile number"})
        else:
            hashed_password_rnds=bcrypt.gensalt(14)
            hashed_password=bcrypt.hashpw(password.encode('utf-8'),hashed_password_rnds).decode('utf-8')
            employee = Employee(
                name=name,
                email=email,
                contact=contact,
                department=department,
                designation=designation,
                password=hashed_password, 
                profile_image=profile_image
            )
            employee.save()
            return JsonResponse({"msg": "User registered successfully"})

@csrf_exempt
def login(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")

        if user_exists(user=username,pswrd=password):
           return JsonResponse({"msg":"logged in successfully"})
        return JsonResponse({"msg":"login api working"})
    