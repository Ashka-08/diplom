from django.core.management.base import BaseCommand
from diplomapp.models import Category


class Command(BaseCommand):
    help = "Create category by name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Category name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        name = name.split('_')
        res = ''
        for i in name:
            res += ' ' + i
        category = Category(name=res)
        category.save()
        self.stdout.write(f'{category}')