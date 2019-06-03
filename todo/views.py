from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets

from todo.models import User, Entry, Book
from todo.serializer import UserSerializer, EntrySerializer


@login_required
def index(request):
    return render(request, 'top.html')


@login_required
def user_info(request):
    return render(request, 'user-info.html')


@login_required
def top(request):
    return render(request, 'top.html')


def test(request):
    Book.objects.raw('')
    # クエリパラメータdataを取得
    d = {
        'data': request.GET.get('data', default='acg')
    }
    return render(request, 'top.html', d)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

