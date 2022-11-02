from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            # return render(request,
            #               'account/register_done.html',
            #               {'new_user': new_user})
            return redirect('music:home')
        else:
            return HttpResponse('Data is not valid')

    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
