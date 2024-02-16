from django.core.management.base import BaseCommand
from diplomapp.models import SubCategory, Category


class Command(BaseCommand):
    help = "Create Subcategory by name and ID category"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Subcategory name')
        parser.add_argument('category_id', type=str, help='Category id')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        name = name.split('_')
        res = ''
        for i in name:
            res += ' ' + i
        
        category_id = kwargs.get('category_id')
        category = Category.objects.filter(id=category_id).first()

        subcategory = SubCategory(name=res, category=category)
        subcategory.save()
        self.stdout.write(f'{subcategory}')
        