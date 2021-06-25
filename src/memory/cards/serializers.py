from rest_framework import serializers

from .models import Card, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'slug',
            'name',
        ]


class CardSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Card
        fields = [
            'id',
            'slug',
            'category',
            'question',
            'answer',
            'question_html',
            'answer_html',
        ]
