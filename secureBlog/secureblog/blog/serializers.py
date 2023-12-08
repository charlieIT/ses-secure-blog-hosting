from django.contrib.auth.models import User, Group
#from rest_framework import serializers
import rest_framework as REST
from rest_framework import serializers
from .models import Post, Comment, Category

class UserSerializer(REST.serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(REST.serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostSerializer(REST.serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'abstract', 'author', 'content', 'created_on', 'updated_on', 'status']