from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
    """Регистрация нового пользователя"""
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.first_name}!')
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    """Вход в аккаунт"""
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'С возвращением, {user.first_name}!')

                # Перенаправляем на страницу, откуда пришли, или на главную
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
        messages.error(request, 'Неверный логин или пароль')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """Выход из аккаунта"""
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта')
    return redirect('/')


def profile_view(request):
    """Личный кабинет"""
    if not request.user.is_authenticated:
        return redirect('users:login')

    # Получаем заказы пользователя (добавим позже)
    orders = []

    context = {
        'user': request.user,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)