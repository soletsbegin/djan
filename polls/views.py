from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from ipware import get_client_ip

from .models import User, UsersEntries


def index(request):
    return render(request, 'polls/index.html')


def test(request):
    return render(request, 'polls/test.html')


def enter(request):
    users_list = User.objects.order_by('login')
    return render(request, 'polls/enter.html', {'users_list': users_list})


def user_info(request, login):
    user = get_object_or_404(User, login=login)
    ip = get_client_ip(request)[0]

    context = {'user': user,
               'ip': ip}
    return render(request, 'polls/user_info.html', context)

