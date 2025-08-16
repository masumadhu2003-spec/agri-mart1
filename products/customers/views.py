from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home.html')
def About(request):
    return render(request,'About.html')
def Login (request):
    return render(request,'Login.html')
def products(request):
    return render(request,'products.html')
def fertilizers(request):
    return render (request,'fertilizers.html')    
def liquids(request):
    return render(request,'liquids.html')
def powders(request):
    return render(request,'powders.html')



from django.shortcuts import render, redirect
from .models import UserAccount
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('Register')

        # Save to database
        UserAccount.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            password=password  # In real apps, hash the password!
        )
        messages.success(request, "Account created successfully")
        return redirect('Login')

    return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserAccount.objects.get(email=email)
            if user.password == password:  # You should hash-check this in real apps!
                request.session['user_id'] = user.id  # Example: simple session login
                messages.success(request, "Login successful")
                return redirect('products')
            else:
                messages.error(request, "Invalid email or password")
        except UserAccount.DoesNotExist:
            messages.error(request, "Invalid email or password")
            
        return redirect('products/')

    return render(request, 'login.html')


def myprofile(request):
    user_id = request.session.get('user_id')  # get the logged-in user ID
    if user_id:
        user = UserAccount.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'myprofile.html', context)
    else:
        return redirect('Login')  
    

def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('Login')
