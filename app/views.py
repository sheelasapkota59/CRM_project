from django.shortcuts import render , render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record 
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def dashboard(request):
    #using Django's ORM (Object-Relational Mapping) to query and retrieve the data in your views.
    #Query all records
    records = Record.objects.all()
    return render(request , 'dashboard.html',{'records' : records})

def login_user(request):
    #check to see if logging in
    if request.method == "POST":
        # username = request.POST.get('username', '')  # Returns an empty string if 'username' key is not present
        # password = request.POST.get('password', '')
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request , username = username , password = password)
        
        #logic
        #after checking username ,password it distinguish whether user to login or not
        if user is not None:
            login(request , user)
            messages.success(request , "You have been logged In!")
            return redirect('dashboard')  #we are redirecting user to home page
        else:
            messages.success(request , "Sorry , your password or username doesnot match")
            return redirect('login')
        
    else:
        
      return render(request , 'login.html' , {})




def logout_user(request):
    logout (request)
    messages.success(request ,"You have been logged out!")
    return redirect('login')

def register_user(request):
    forms = SignUpForm()
    #if user are sending post request to fillup form then this action act
    if request.method == 'POST':
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            #if form is valid then
            forms.save()
            #authenticate and login
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request , user)
            messages.success(request,"You have successfully registered")
            return redirect('login')
        else:
            #if form isnot valid then
            forms = SignUpForm()
            messages.success(request , "Your provided information doesnot match the required credentials")
            return render(request , 'register.html' , {'forms' : forms})
    else:   
        return render(request , 'register.html' , {'forms' : forms})
    

def reset_password(request):
    pass

def customer_record(request , pk):
    if request.user.is_authenticated:
        #look up Records
        customer_record = Record.objects.get(id = pk)
        return render(request , 'record.html' , {'customer_record' : customer_record})
    else:
        messages.success(request , "You must be login!!")
        return redirect('login')
    
    
def delete_record(request , pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request , "You  successfully deleted your data")
        return redirect('dashboard')
    else:
        messages.success(request , "you must logged in first!!")
        return redirect('login')


def add_record(request):
    forms = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if forms.is_valid():
                add_record = forms.save()
                messages.success(request , "Record Added...")
                return redirect('dashboard')
        return render(request , 'add_record.html' ,{'forms':forms})
    else:
       messages.success(request , "You Must be logged In......")
       return redirect('login')
   
def update_record(request , pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        
        #to update the form , we should have existing fillup form so that we can edit on it ,
        #here , instance = current_current is making possible for us to get existing data where we want to update
        form = AddRecordForm(request.POST or None, instance=current_record)
        
        if request.method == 'POST':
        #if they are doing nthg(None) then ok , but if they want to POST then check valid or not 
            if form.is_valid():
                form.save()
                messages.success(request , "Record has been updated")
                return redirect('dashboard')
            else:
                return render(request , 'update_record.html' , {'form': form})
        
        else:
            # If it's not a POST request, render the form
            return render(request, 'update_record.html', {'form': form})

    
    else:
        messages.success(request , "You Must be logged In......")
        return redirect('login')
        
        
        
        

        