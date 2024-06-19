from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Zalogowano poprawnie")
            return redirect('home')
        else:
            messages.error(request, "Wystąpił błąd podczas logowania, spróbuj ponownie!")
            return redirect('home')

    # If not logging in, if logged in 
    else:
        return render(request, 'home.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano poprawnie")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Zarejestrowano pomyślnie')
            
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    # Checking if logged in 
    if request.user.is_authenticated:
        # Looking up record
        customer_record = Record.objects.get(id=pk)
    
        return render(request, 'record.html', {'customer_record': customer_record})
    
    # If not logged in
    else:
        messages.success(request, "Aby zobaczyć tę stronę, musisz być zalogowany")
        return redirect('home')
    
def delete_record(request, pk):
    delete_it = Record.objects.get(id = pk)
    delete_it.delete()
    messages.success(request, "Klient usunięty poprawnie.")
    return redirect('home')