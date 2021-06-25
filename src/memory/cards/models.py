from django.db import models
from django.utils.translation import ugettext_lazy as _
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=64, unique=True)
    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Card(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        on_delete=models.PROTECT,
        related_name='cards',
        related_query_name='card',
    )
    question = models.TextField(_('Question'))
    slug = models.SlugField(_('Slug'), unique=True)
    answer = models.TextField(_('Answer'))
    question_html= models.TextField(_('Question HTML'))
    answer_html = models.TextField(_('Answer HTML'))

    def __str__(self):
        return f'{self.category}: {self.question}'

    def save(self, *args, **kwargs):
        self.question_html = highlight(self.question, PythonLexer(), HtmlFormatter())
        self.answer_html = highlight(self.answer, PythonLexer(), HtmlFormatter())
        super().save(*args, **kwargs)
