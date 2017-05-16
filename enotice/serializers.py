from rest_framework import serializers
from enotice.models import Post
from advertisment.models import Adv

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('teacher', 'title', 'description', 'created_date', 'published_date')

class AdvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adv
        fields = ('item_name', 'item_desc', 'old_price', 'new_price', 'created_date', 'published_date')
