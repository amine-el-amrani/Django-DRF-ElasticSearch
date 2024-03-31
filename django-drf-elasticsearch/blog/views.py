from django.shortcuts import render
from rest_framework import viewsets

from blog.models import Article, Category, User
from blog.serializers import ArticleSerializer, CategorySerializer, UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()