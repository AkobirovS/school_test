from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    context = {}
    return render(request, 'index.html',context)