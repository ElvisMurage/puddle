from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from .models import EmailVerificationToken
from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from item.models import Category, Item
from .forms import SignupForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
         'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/Terms_of_service.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save()
            user.save()

            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form':form
    })
def logout(request):
    logout(request)
    return render('loggedout.html')
