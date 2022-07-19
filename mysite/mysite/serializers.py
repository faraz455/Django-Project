from rest_framework import serializers
from service.models import Service
from news.models import News

class NewsSerializer(serializers.Serializer):
    news_title = serializers.CharField()
    news_des = serializers.CharField()
    
    def create(self, validated_data):
        return News.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        News.objects.filter(id= instance.id).update(**validated_data)
        return News.objects.get(id = instance.id)