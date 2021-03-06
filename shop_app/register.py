from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from shop_app.forms import RegisterForm

def register_page(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           # save user
           user = User.objects.create_user(
                        username = form.cleaned_data['username'],
                        password = form.cleaned_data['password'],
                        email = form.cleaned_data['email']
                    )

           # and redirect to /registration_sucess
           return HttpResponseRedirect("/register/success")

    return render(request, "login.html", {
        'form' : form
        })

def register_success(request):
    #return render(request, "registration/register_success.html")
    return HttpResponse("Register success")

def logout(request):
    logout(request)
    return HttpResponseRedirect("/")
