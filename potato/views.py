from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'potato/main.html')

class LoginView(View):
    pass

class LogoutView(View):
    pass

class RegisterView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        return render(request, 'potato/register.html', {'form': form})

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'potato/register.html', {'form': form})
