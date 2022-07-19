from curses import meta
from rest_framework import serializers
from service.models import Service
from news.models import News

# The below commented part is basic work in which you specify the
    # Create update and rest http methods manually

## class NewsSerializer(serializers.Serializer):
##     news_title = serializers.CharField()
##     news_des = serializers.CharField()
    
##     def create(self, validated_data):
##         return News.objects.create(**validated_data)
    
##     def update(self, instance, validated_data):
##         News.objects.filter(id= instance.id).update(**validated_data)
##         return News.objects.get(id = instance.id)

# It takes ModelSerializer in this you dont need to specify any fiel it taks only 2 things
    # Model name and fields which can be written manually or just write "__all__"
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


