from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from .serializer import UserSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'message':'sucsesful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(self.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    context = {}
    return render(request, 'index.html',context)