import argparse
import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from memory.cards.models import Card, Category


class Command(BaseCommand):
    help = 'Import cards from csv'

    def add_arguments(self, parser):
        parser.add_argument(
            dest='csv_file',
            type=argparse.FileType(),
            help='CSV file name.',
        )

    def import_card(self, row):
        category, _ = Category.objects.get_or_create(
            name=row['category'],
            slug=slugify(row['category']),
        )
        Card.objects.update_or_create(
            question=row['question'],
            slug=slugify(row['question']),
            answer=row['answer'],
            category=category,
        )

    def handle(self, *args, **options):
        reader = csv.DictReader(options['csv_file'], delimiter=';')
        for row in reader:
            self.import_card(row)

        self.stdout.write(self.style.SUCCESS('Import successfull!'))
        self.stdout.write(self.style.SUCCESS('-' * 19))
        for category in Category.objects.all():
            self.stdout.write(self.style.SUCCESS(
                f'{category.name}: {category.cards.count()}'
            ))
