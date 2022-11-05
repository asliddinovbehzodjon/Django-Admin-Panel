from django.shortcuts import render
from .models import BotUsers
from rest_framework.response import Response
from .serializer import BotUserSerailizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
# Create your views here.
class BotUserViewset(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerailizer
class Change(APIView):
    def get(self,request,id,lang):
        user = BotUsers.objects.filter(telegram_id=id).update(language=lang)
        return Response({'status':'Ok'})