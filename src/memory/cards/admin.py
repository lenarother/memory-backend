from django.contrib import admin

from .models import Card, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'name'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'slug',
        'answer',
        'category'
    ]
    list_filter = ['category']
    readonly_fields = [
        'question_html',
        'answer_html'
    ]
    prepopulated_fields = {'slug': ('question',)}
