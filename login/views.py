from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):  # no repeat log in
        return redirect('/index/')

    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'Please check the information!'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(username=username)
            except:
                message = 'User not exist！'
                return render(request, 'login/login.html', locals())



            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = 'Incorrect password！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # user must log in
        return redirect("/login/")
    request.session.flush()

    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")