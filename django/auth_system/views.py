from secrets import randbits as _randbits
from traceback import print_exc

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm
from .models import User_SEED
from _sha256 import sha256
from .algorithm import shuffle
from math import pow


def index(request):
    return render(request, 'auth_system/index.html')


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('index')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('index')
    else:
        return render(request, 'auth_system/login.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/auth_system/index')


def User_register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        register_user = User.objects.create_user(
            username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
        user_s = User_SEED.objects.create(
            user=register_user, name='Auth System')
        register_user.save()
        user_s.save()
        return HttpResponseRedirect('/auth_system/index')
    else:
        return render(request, 'auth_system/register.html', {'form': form})


@csrf_exempt
def Server_create_SEED(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/auth_system/index')
    user_name = request.POST.get('username', '')
    client_random = request.POST.get('client random', '')
    try:
        user_obj = User.objects.get(username=user_name)
        user_seed = User_SEED.objects.get(user=user_obj)
        serv_random = _randbits(256)
        user_seed.Server_Random = str(serv_random)
        user_seed.Client_Random = str(client_random)
        # something make trouble, maybe the SEED. this way i let SEED < 10^9.
        user_seed.SEED = int(sha256(
            f'{client_random}{serv_random}'.encode()).hexdigest(), 16) % pow(10, 9)
        user_seed.save()
        li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']*8
        ll = shuffle.fisher_yates_shuffle(li, int(user_seed.SEED))
        print(li)

        return HttpResponse(serv_random)
    except:
        print_exc()
        pass
    return render(request, 'auth_system/Server_Random.html', locals())
