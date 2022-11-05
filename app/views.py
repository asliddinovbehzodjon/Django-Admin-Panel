from django.shortcuts import render
from .models import BotUsers,Image
from rest_framework.response import Response
from .serializer import BotUserSerailizer,ImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
# Create your views here.
class BotUserViewset(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerailizer
class ImageViewset(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
class Change(APIView):
    def get(self,request,id,lang):
        user = BotUsers.objects.filter(telegram_id=id).update(language=lang)
        return Response({'status':'Ok'})