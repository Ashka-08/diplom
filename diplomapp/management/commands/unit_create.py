from django.core.management.base import BaseCommand
from diplomapp.models import Unit


class Command(BaseCommand):
    help = "Create unit by name"

    def add_arguments(self, parser):
        parser.add_argument('unit_of_measurement', type=str, help='Unit name')

    def handle(self, *args, **kwargs):
        unit_of_measurement = kwargs.get('unit_of_measurement')
        unit = Unit(unit_of_measurement=unit_of_measurement)
        unit.save()
        self.stdout.write(f'{unit}')