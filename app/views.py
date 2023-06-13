from django.shortcuts import render, redirect
from .models import Food,Consume,Login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
    
    
def index(request):
        return render(request, 'app/home.html')    

def home(request):
     
    if request.method =="POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
     
     
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
     
    return render(request,'app/index.html',{'foods':foods,'consumed_food':consumed_food})
     
def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'app/delete.html')

def calculator(request):
    if request.method == 'POST':
        weight = request.POST['weight']
        height = request.POST['height']
        age = request.POST['age']
        gender = request.POST['gender']
        print("weight: ",weight)
        print("height: ",height)
        print("age: ",age)
        print("gender: ",gender)
        if gender == 'male':
            result = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
            print(result,"######################")
            return render(request,'app/calculator.html',{'result':result})
        if gender == 'female':
            result = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))
            print(result,"######################") 
            return render(request,'app/calculator.html',{'result':result})
    return render(request,'app/calculator.html')
     
# def register(request):
#     if request.method == 'POST':
#         username  = request.POST['username ']
#         password = request.POST['password']
#         Login.objects.create(username =username ,password=password)
#         return render(request, 'app/register.html')
#     return render(request, 'app/register.html') 

# def login(request):
#     if request.method == 'POST':
#         username  = request.POST['username ']
#         password = request.POST['password']
#         user = Login.objects.filter( username = username , password=password).exists()
#         if user:
#             # request.session['username']= user.username 
#             return render(request, 'app/index.html', {'username': username})
#         else:
#             return render(request, 'app/register.html')
#     return render(request, 'app/register.html')
    
# def logout_view(request):
#     logout(request)
#     return render(request, 'app/register.html')