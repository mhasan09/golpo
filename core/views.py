from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import POST, UserProfile
from django.shortcuts import get_object_or_404


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


@login_required
def feed(requests):
    user_id_list = [requests.user.id]
    current_user = requests.user
    for i in current_user.UserProfile.follows.all():
        user_id_list.append(i.user.id)
    posts = POST.objects.filter(created_by_id__in=user_id_list)
    query = requests.GET.get('query', '')
    if len(query) > 0:
        users = User.objects.filter(username__icontains=query)
    else:
        users = []
    for post in posts:
        likes = post.likes.filter(created_by_id=requests.user.id)
        if likes.count() > 0:
            post.liked = True
        else:
            post.liked = False

    context = {
        "username": current_user,
        "posts": posts,
        'query': query,
        'users': users
    }
    return render(requests, 'core/feed.html', context)


def profile(requests, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(requests, 'core/profile.html', context)


@login_required
def follow_profile(requests, username):
    user = get_object_or_404(User, username=username)
    requests.user.userprofile.follows.add(user.userprofile)
    return redirect('profile', username=username)


@login_required
def unfollow_profile(requests, username):
    user = get_object_or_404(User, username=username)
    requests.user.userprofile.follows.remove(user.userprofile)
    return redirect('profile', username=username)


def followers(requests, username):
    user = get_object_or_404(User, username=username)
    return render(requests, 'core/followers.html', {'user': user})


def follows(requests, username):
    user = get_object_or_404(User, username=username)
    return render(requests, 'core/follows.html', {'user': user})


@login_required
def edit_profile(requests):
    if requests.method == "POST":
        form = UserProfileForm(requests.POST, requests.FILES, instance=requests.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=requests.user.username)

    else:
        form = UserProfileForm(instance=requests.user.userprofile)

    context = {
        'user': requests.user,
        'form': form
    }
    return render(requests, 'core/edit_profile.html', context)
