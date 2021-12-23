from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticlesForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .models import Category, Product


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')



def classes(request):
    return render(request, 'main/classes.html')


def contactus(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("{% url 'contactus'%}")
        else:
            error = 'ERROR'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/contactus.html', data)


def schedules(request):
    return render(request, 'main/schedules.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'main/signup.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect("{% url 'signup'%}")
    context = {'form': form}

    return render(request, 'main/register.html', context)


def logout(request):
    logout(request)

