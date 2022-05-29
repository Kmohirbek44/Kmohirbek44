from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt
import scraping.models
import json
import requests
from django.contrib.messages import constants as message_tag
from .form import UserLoginForm, register, profile, ContactForm, UserUpdateForm
from django.contrib import messages



User=get_user_model()
def register_login(request):
    if request.method == 'POST':
        formregister = register(data=request.POST)
        if formregister.is_valid():
            formregister.save()

            messages.success(request, 'succesfuly register')

            return HttpResponseRedirect(reverse('accounts:login'))

    else:

        formregister = register()
    context = {'form': formregister}

    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            try:
                login(request, user)
            except Exception:
                return HttpResponseRedirect(reverse('accounts:update'))
            return HttpResponseRedirect(reverse('accounts:update'))
    else:
        form=UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('scraping:home'))


@login_required
def user_update_view(request):
    user = request.user
    data = scraping.models.Resume.objects.filter(email=user.email).first()
    if request.method == 'POST':

        form = profile(data=request.POST,files=request.FILES,instance=request.user)

        if form.is_valid():
            data = form.cleaned_data
            print('data:',data)

            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.username = data['username']
            user.save()
            return HttpResponseRedirect(reverse('accounts:update'))
        else:
            data = form.cleaned_data
            print('data:', data)

            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.username = data['username']
            user.save()
            return HttpResponseRedirect(reverse('accounts:update'))

    else:
        form = profile(instance=request.user)


    return render(request, 'accounts/profile.html', {'formone': form, 'ContactForm': ContactForm,'formuser': UserUpdateForm,'data':data})


def delete_user(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method=='POST':
            qs=User.objects.filter(pk=user.pk)
            qs.delete()
    return HttpResponseRedirect(reverse('scraping:home'))
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST or None)
        if form.is_valid():
            data=form.cleaned_data
            city=data.get('city')
            language=data.get('language')
            username=data.get('username')

            qs = scraping.models.Errors.objects.filter(timestap=dt.date.today())


            if qs.exists():
                err=qs.first()
                data=err.data.get('user_data',[])
                data.append({'city':city,'language':language,'username':username})
                err.data['user_data']=data
                err.save()

                messages.add_message(request, messages.SUCCESS, "Sizning so'rovingiz adminga jo'natildi")
                return HttpResponseRedirect(reverse('accounts:update'))
            else:
                data=[{'city':city,'language':language,'username':username}]
                date={'user_data':data}
                scraping.models.Errors(data=date).save()

                messages.add_message(request, messages.SUCCESS, 'Yuborildi')
                return HttpResponseRedirect(reverse('accounts:update'))

        else:
            return redirect('accounts:update')

    else:
        return redirect('accounts:login')

def choice(request):
    user = request.user
    if request.method == 'POST':
       formuser = UserUpdateForm(request.POST, initial={'city': user.city, 'language': user.language,
                                                     'send_email': user.send_email})
       if formuser.is_valid():
           data = formuser.cleaned_data
           user.city = data['city']
           user.language = data['language']
           user.send_email = data['send_email']
           user.save()
           return HttpResponseRedirect(reverse('accounts:update'))

    return HttpResponseRedirect(reverse('accounts:update'))


