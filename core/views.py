from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from .models import POST


@login_required
def feed(requests):
    user_id_list = [requests.user.id]
    current_user = requests.user
    for i in current_user.UserProfile.follows.all():
        user_id_list.append(i.user.id)
    posts = POST.objects.filter(created_by_id__in=user_id_list)
    context = {
        "username": current_user,
        "posts": posts
    }
    return render(requests, 'core/feed.html', context)


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

    return render(request, 'core/sign-up.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')

    return render(request, 'core/sign-in.html')
