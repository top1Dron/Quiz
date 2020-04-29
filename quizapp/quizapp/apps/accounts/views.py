from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .services import UserServices

services = UserServices()

class UserRegister(View):
    def post(self, request):
        newUser, userForm, profileForm = services.postRegisterUser(request)
        if newUser:
            return render(request, 'accounts/registration_complete.html', {
                'new_user': newUser,
            })
        return self.registerRender(request, 'accounts/register.html', userForm, profileForm)
        


    def get(self, request):
        userForm, profileForm = services.getRegisterUser()
        return self.registerRender(request, 'accounts/register.html', userForm, profileForm)

    def registerRender(self, request, page, user_form, profile_form):
        return render(request, page, {'user_form':user_form, 'profile_form':profile_form})

class UserEdit(View):
    """view for editing user profile data. Includes fields from User and Profile tables"""

    
    def get(self, request):
        userForm, profileForm = services.getEditUser(request)
        return render(
            request,
            'accounts/edit.html', {
                'user_form': userForm,
                'profile_form': profileForm,
                'user': request.user
            },
        )


    def post(self, request):
        services.postEditUser(request)
        return redirect('subjects:list')


def validate_username(request):
    """view for ajax checking username available"""

    username = request.GET.get('username', None)
    data = {
        'is_taken' : services.checkIsUsernameAvailable(username)  
    }
    return JsonResponse(data)


def register_validate_email(request):
    """view for ajax checking email available in register"""

    email = request.GET.get('email', None)
    data = {
        'is_taken' : services.checkIsEmailAvailable(email)
    }
    return JsonResponse(data)


def edit_validate_email(request):
    """view for ajax checking email available in edit"""

    email = request.GET.get('email', None)
    data = {
        'is_taken' : services.checkIsEmailAvailableForExistUser(email, request.user)
    }
    return JsonResponse(data)