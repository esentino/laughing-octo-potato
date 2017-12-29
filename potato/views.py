from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'potato/main.html')

class LoginView(View):
    pass

class LogoutView(View):
    pass

class RegisterView(View):
    pass