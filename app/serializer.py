from rest_framework import serializers
from .models import BotUsers,Image
class BotUserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = "__all__"
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'