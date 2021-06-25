from rest_framework import viewsets

from .models import Card, Category
from .serializers import CardSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('?')
    serializer_class = CardSerializer
